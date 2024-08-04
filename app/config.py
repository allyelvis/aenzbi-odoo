class Config:
    SECRET_KEY = 'your_secret_key'
    FLASK_ENV = 'development'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///your_database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # To disable Flask-SQLAlchemy event system
    # Add more configurations as needed
