import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'defaultsecretkey')
    DEBUG = os.getenv('DEBUG', 'True') == 'True'
