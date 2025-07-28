from flask import Flask, render_template, request, redirect, session, send_file
from pymongo import MongoClient
import io

app = Flask(__name__)
app.secret_key = 'kalro-secret-key'

# MongoDB setup
client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000")
client.admin.command('ping')  # Check connection
db = client.Kalro_db
admins = db.admins
purchased = db.purchased
users = db.users

# Login route
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        admin = admins.find_one({'username': username, 'password': password})

        if admin:
            session['username'] = username
            session['location_id'] = admin['location_id']
            return redirect('/dashboard')
        else:
            error = "Invalid credentials"

    return render_template('login.html', error=error)

# Dashboard route
@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect('/')

    # Only show all completed purchases that are either included or declined for transport
    query = {
        "status": "completed",
        "transport_checkout_status": {"$in": ["included", "declined"]}
    }

    records = list(purchased.find(query))
    print(records)

    return render_template(
        "dashboard.html",
        username=session['username'],
        records=records,
        admin={"username": session['username']}
    )
# Download report route

# Logout route
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
