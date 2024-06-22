from flask import Flask
import flask_monitoringdashboard as dashboard


# Create Flask application instance
app = Flask(__name__)
dashboard.bind(app)


# Load configuration from config.py
app.config.from_pyfile('../config.py')

# Import routes to set up the application
from app import routes