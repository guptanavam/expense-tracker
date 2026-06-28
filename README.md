**🔗 Live Demo:** https://expense-tracker-2xrb.onrender.com/

# Expense Tracker

A simple web app to track personal expenses, built with Flask and SQLite. Users can add, edit, delete, and view expenses, with an automatically calculated running total.

## Features

- Add new expenses with description, amount, and category
- View all expenses in a sortable, styled table
- Edit existing expenses
- Delete expenses
- Persistent storage using SQLite — data survives server restarts
- Responsive UI built with Bootstrap

## Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite
- **Frontend:** HTML, Bootstrap 5
- **Templating:** Jinja2

## How to Run Locally

1. Clone this repository
git clone https://github.com/guptanavam/expense-tracker.git

cd expense-tracker

2. Install dependencies
pip install -r requirements.txt

3. Initialize the database
python database.py

4. Run the app
python app.py

5. Open your browser to `http://localhost:5000`

## Screenshots

(Screenshots will be added here once available)

## What I Learned

Building this project helped me understand how web applications connect a frontend, backend, and database together — specifically handling form submissions, writing parameterized SQL queries to prevent injection attacks, and structuring a Flask app with multiple interacting routes.

## Future Improvements

- Add user authentication so multiple people can track separate expenses
- Add monthly/category-based spending charts
- Deploy to a cloud platform for public access
- Move to a persistent hosted database (e.g., PostgreSQL) — currentSQLite
  may reset on free-tier hosting restarts