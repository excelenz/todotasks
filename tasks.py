from flask import Flask,jsonify,redirect,request
from datetime import datetime
from models import db, Tasks, TasksSchema

def main(id,request):
    import datetime
    Task = Tasks.query.order_by(Tasks.time_create.desc())
    tasks_schema = TasksSchema(many=True)
    resp=tasks_schema.dump(Task)
    return resp
