from flask import Flask
from marshmallow import Schema, fields, pre_load, validate,post_dump
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import mysql.connector
import os
import sqlalchemy

ma = Marshmallow()
db = SQLAlchemy()

HOST = "35.205.107.137:3306"
cloud_sql_connection_name = "to-do-list-309620:europe-west1:todolist"
PASSWORD ="qwerty12"

if (os.getenv('SERVER_SOFTWARE') and os.getenv('SERVER_SOFTWARE').startswith('Google App Engine/')):
  db = mysql.connector.connect(host='localhost', user='root',password=PASSWORD)
else:
    db_config = {
        "pool_size": 5,
        "max_overflow": 2,
        "pool_timeout": 30,  # 30 seconds
        "pool_recycle": 1800,  # 30 minutes
    }
    db_user = 'root'
    db_pass = 'qwerty12'
    db_name = 'todolist'
    db_socket_dir = '/cloudsql'
    cloud_sql_connection_name = "to-do-list-309620:europe-west1:todolist"
    pool = sqlalchemy.create_engine(

        sqlalchemy.engine.url.URL(
            drivername="mysql+pymysql",
            username=db_user,  # e.g. "my-database-user"
            password=db_pass,  # e.g. "my-database-password"
            database=db_name,  # e.g. "my-database-name"
            query={
                "unix_socket": "{}/{}".format(
                    db_socket_dir,  # e.g. "/cloudsql"
                    cloud_sql_connection_name)  # i.e "<PROJECT-NAME>:<INSTANCE-REGION>:<INSTANCE-NAME>"
            }
        ),
        **db_config
    )
    # [END cloud_sql_mysql_sqlalchemy_create_socket]



class Tasks(db.Model):
    __tablename__ = 'tasks'
    task_id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(255),nullable=False)
    time_create = db.Column(db.String)
    status = db.Column(db.Integer, default = 0)
    def __repr__(self):
        return '<Tasks {}>'.format(self.task_name)

class TasksSchema(ma.Schema):
    task_id = fields.Int()
    task_name = fields.Str()
    status = fields.Int()
    time_create = fields.Method("format_date", dump_only=True)
    ordered=True
    def format_date(self, Tasks):
        return Tasks.time_create
