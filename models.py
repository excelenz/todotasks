from flask import Flask
from marshmallow import Schema, fields, pre_load, validate,post_dump
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import sqlalchemy

ma = Marshmallow()
db = SQLAlchemy()


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
