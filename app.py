from flask import Flask, render_template, request, redirect, url_for
from db import db
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bracket_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/signup', methods=['GET'])
def signup_form():
    # Import models only when needed in the route
    from models.user import User
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    from models.user import User

    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    password_hash = generate_password_hash(password)

    new_user = User(username=username, email=email, password_hash=password_hash)
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    from models.user import User

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Hash the password
        hashed_password = generate_password_hash(password, method='sha256')

        # Add the user to the database
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('register.html')

@app.route('/')
def home():
    return {"message": "Welcome to the College Football Bracket App!"}

@app.before_request
def create_tables():
    if not hasattr(app, 'has_run'):
        db.create_all()
        app.has_run = True

if __name__ == "__main__":
    app.run(debug=True, port=5002)


if __name__ == "__main__":
    with app.app_context():
        print("Database Initialized:", bool(db))
    app.run(debug=True, port=5001)
