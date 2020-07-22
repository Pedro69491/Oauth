from flask_bcrypt import Bcrypt # Initialize bcrypt in my app
from flask_app import app, db
import datetime
import jwt # In order to create the the token


bcrypt = Bcrypt(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80), unique=True)
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8') # turn it in a string instead of byte
        self.registered_on = datetime.datetime.now()

    def __repr__(self):
        return self.username

    # it generates the Auth token
    def encode_auth_token(self, user_id):
        try:
            payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5), # expiration date of the token
            'iat': datetime.datetime.utcnow(), # the time the token is generated
            'sub': user_id # the subject of the token (the user whom it identifies)
            }
            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm= 'HS256' # The algorithm which encodes header, payload, and secretkey
            )
        except Exception as e:
            return e


    

