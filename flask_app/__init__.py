# file with the task to initialize the app
from flask_sqlalchemy import SQLAlchemy # layer between object oriented Python and the database
from flask import Flask


app = Flask(__name__)


POSTGRES = {
    'user': 'postgres',
    'pw': '135792468',
    'db': 'flaskExperiment',
    'host': 'localhost',
    'port': '5432'
}

# config is the place where Flask stores configuration values, config is an atribute of the flask object
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES # Connect the app with the database using SQLALCHEMY
app.config.from_object('config.Config') # Application Configuration

db = SQLAlchemy(app) # Initializing a database object # connect SQLAlchemy object with my application





# It has to be imported after initializing the app to avoid an import error
from flask_app import routes  





