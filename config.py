import os

# Flask configuration
DEBUG = True  # Enable debug mode (set to False in production)
SECRET_KEY = 'your_secret_key'  # Secret key for session management, CSRF, etc.

# PostgreSQL database configuration
DB_NAME = os.getenv('DB_NAME', 'f1_db')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'admin')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')

