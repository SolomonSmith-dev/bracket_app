# Import necessary modules
from flask import Blueprint, request
from werkzeug.security import generate_password_hash  # For hashing passwords
from app import db  # Import db from app.py to interact with the database
from models.user import User  # Import the User model

# Create a blueprint for authentication-related routes
auth_bp = Blueprint('auth', __name__)

# Define the signup route to register new users
@auth_bp.route('/signup', methods=['POST'])  # Only allow POST requests for signup
def signup():
    # Get the data sent in the POST request body as JSON
    data = request.get_json()
    
    # Hash the password provided by the user for security
    hashed_password = generate_password_hash(data['password'])
    
    # Create a new User object with the data received
    new_user = User(username=data['username'], email=data['email'], password_hash=hashed_password)
    
    # Add the new user to the database session
    db.session.add(new_user)
    
    # Commit the changes to save the new user in the database
    db.session.commit()
    
    # Return a success message
    return {"message": "User created successfully"}, 201  # HTTP status 201 indicates resource was created
