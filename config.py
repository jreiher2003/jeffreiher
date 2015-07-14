import os

WTF_CSRF_ENABLED = True
SECRET_KEY = "secret"

# email server
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('jeffreiher@gmail.com')
MAIL_PASSWORD = os.environ.get('finn7797')

# administrator list
ADMINS = ['jeffreiher@gmail.com']