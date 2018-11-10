import os

DEBUG = os.getenv('DEBUG') in ['True', 'true', '1', 'yes']
if DEBUG:
    SQLALCHEMY_ECHO = True

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

LOG_LEVEL = os.getenv('LOG_LEVEL') or 'debug'
SERVICE_NAME = os.getenv('SERVICE_NAME') or 'TasteAI'

SECRET_KEY = os.getenv('SECRET_KEY')
NONCE_SECRET = os.getenv('NONCE_SECRET')
HASHIDS_SALT = os.getenv('HASHIDS_SALT')
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
BASE_URL = os.getenv('BASE_URL')
GENERAL_INFO_EMAIL = os.getenv('GENERAL_INFO_EMAIL')
CDN_URL = os.getenv('CDN_URL')
GIPHY_API_KEY = os.getenv('GIPHY_API_KEY')