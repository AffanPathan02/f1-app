from flask import Flask

# Create Flask application instance
app = Flask(__name__)

# Load configuration from config.py
app.config.from_pyfile('../config.py')

# Import routes to set up the application
from app import routes