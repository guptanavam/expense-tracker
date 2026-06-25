from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("expenses.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return render_template("home.html")

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

@app.route("/expenses")
def view_expenses():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    all_expenses = cursor.fetchall()
    conn.close()

    total = sum(expense["amount"] for expense in all_expenses)

    return render_template("expenses.html", expenses=all_expenses, total=total)

if __name__ == "__main__":
    app.run(debug=True)