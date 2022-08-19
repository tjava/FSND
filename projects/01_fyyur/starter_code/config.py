import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
# SQLALCHEMY_DATABASE_URI = '<Put your local database url>'
# SQLALCHEMY_DATABASE_URI = 'postgresql://nano1:1234@localhost:5432/nanodb'
SQLALCHEMY_DATABASE_URI = 'postgresql://nano:Password@postgresql-85650-0.cloudclusters.net:10487/new'