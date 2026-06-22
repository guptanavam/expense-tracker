from flask import Flask, render_template, request, redirect

app = Flask(__name__)

expenses = []   # temporary storage — lives only while the server runs

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/add", methods=["POST"])
def add_expense():
    description = request.form["description"]
    amount = request.form["amount"]
    category = request.form["category"]
    expense = {
        "description": description,
        "amount": float(amount),
        "category": category
    }
    expenses.append(expense)
    
    print(expenses)

    return redirect("/")
@app.route("/expenses")
def view_expenses():
    total = sum(expense["amount"] for expense in expenses)
    return render_template("expenses.html", expenses=expenses, total=total)


if __name__ == "__main__":
    app.run(debug=True)

