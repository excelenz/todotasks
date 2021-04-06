from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
import secret

db_user = secret.db_user
db_pass = secret.db_pass
db_name = secret.db_name
db_host = secret.db_host
db_socket_dir = secret.db_socket_dir
cloud_sql_connection_name = secret.cloud_sql_connection_name

SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True

if os.environ.get("DB_HOST"):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@/{}?unix_socket=/{}/{}".format(db_user,db_pass,db_name,db_socket_dir,cloud_sql_connection_name)
else:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}/{}".format(db_user,db_pass,db_host,db_name)
SECRET_KEY = "sdsdsdsdsd-dsdsd-sdshgf£32423423443"
