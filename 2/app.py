
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Atlas connection
client = MongoClient("mongodb+srv://panwarkulde_user:XefIx8H54sQt6@cluster0.a4ro.mongodb.net/?appName=Cluster0")
db = client["student_db"]
collection = db["students"]

# Form page
@app.route('/')
def form():
    return render_template('form.html')

# Handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        grade = request.form['grade']

        # Insert into MongoDB
        collection.insert_one({
            "name": name,
            "grade": grade
        })

        return redirect(url_for('success'))

    except Exception as e:
        return render_template('form.html', error=str(e))

# Success page
@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
