from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("expenses.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()


# ---------- READ routes ----------

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/expenses")
def view_expenses():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses ORDER BY id DESC")
    all_expenses = cursor.fetchall()
    conn.close()

    total = sum(expense["amount"] for expense in all_expenses)

    return render_template("expenses.html", expenses=all_expenses, total=total)


# ---------- CREATE route ----------

@app.route("/add", methods=["POST"])
def add_expense():
    description = request.form["description"]
    amount = request.form["amount"]
    category = request.form["category"]

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO expenses (description, amount, category) VALUES (?, ?, ?)",
        (description, float(amount), category)
    )
    conn.commit()
    conn.close()

    return redirect("/")


# ---------- UPDATE routes ----------

@app.route("/edit/<int:expense_id>")
def edit_expense(expense_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses WHERE id = ?", (expense_id,))
    expense = cursor.fetchone()
    conn.close()

    return render_template("edit.html", expense=expense)


@app.route("/update/<int:expense_id>", methods=["POST"])
def update_expense(expense_id):
    description = request.form["description"]
    amount = request.form["amount"]
    category = request.form["category"]

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE expenses SET description = ?, amount = ?, category = ? WHERE id = ?",
        (description, float(amount), category, expense_id)
    )
    conn.commit()
    conn.close()

    return redirect("/expenses")


# ---------- DELETE route ----------

@app.route("/delete/<int:expense_id>")
def delete_expense(expense_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()
    return redirect("/expenses")


if __name__ == "__main__":
    port = int (os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)