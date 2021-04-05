from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os


#from flask_sqlalchemy import SQLAlchemy
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/db.sqlite3"
#db = SQLAlchemy(app)


SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "sqlite:///tmp/db.sqlite3"


SECRET_KEY = "sdsdsdsdsd-dsdsd-sdshgf£32423423443"
