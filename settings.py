EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('gmail_username') # flake8: noqa 
EMAIL_HOST_PASSWORD = os.environ.get('gmail_password') # flake8: noqa
EMAIL_PORT = 587
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_USE_TLS = True
