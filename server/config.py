import os
import connexion
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

# Create the Connexion application instance
connex_app = connexion.App(__name__, specification_dir=os.path.join(basedir, "swagger/"))

# Get the underlying Flask app instance
app = connex_app.app

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "db/YATI.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '9OLWxND4o83j4KYATI4iuopO'

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)
db.engine.execute('pragma foreign_keys=ON') # Solves SQLite problem with foreign keys, removes SQLite 2 backward compatibility

# Initialize Marshmallow
ma = Marshmallow(app)

# Initialize login module
lm = LoginManager()