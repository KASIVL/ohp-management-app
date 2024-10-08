from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# Database connection setup
conn = psycopg2.connect(
    dbname="master",
    user="postgres",
    password="@Mushui08",
    host="localhost",
    port='5432'
)
cursor = conn.cursor()

# Home route
@app.route('/')
def home():
    return render_template('index.html')  # Renders the index.html template

# Additional routes can be added here

if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask application