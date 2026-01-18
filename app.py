from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect("feedback.db")
    conn.row_factory = sqlite3.Row
    return conn

# Create table
conn = get_db_connection()
conn.execute("""
CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    message TEXT
)
""")
conn.commit()
conn.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    message = request.form["message"]

    conn = get_db_connection()
    conn.execute("INSERT INTO feedback (name, message) VALUES (?, ?)",
                 (name, message))
    conn.commit()
    conn.close()

    return redirect("/")

@app.route("/view")
def view():
    conn = get_db_connection()
    feedbacks = conn.execute("SELECT * FROM feedback").fetchall()
    conn.close()
    return render_template("view.html", feedbacks=feedbacks)

if __name__ == "__main__":
    app.run(debug=True)
