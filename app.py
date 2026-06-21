from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    fruits = ["apple", "banana", "mango"]
    return render_template("home.html", name="Rahul", fruits=fruits)
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)