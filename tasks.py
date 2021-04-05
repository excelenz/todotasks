from flask import Flask,jsonify,redirect,request
from datetime import datetime
from models import db, Tasks, TasksSchema
import logging
import json
import pytz
from datetime import datetime

tzinfo = pytz.timezone('Israel')
logger = logging.getLogger(__name__)
logger.info("*************************************************************** \n ")
logger.info(__name__)

def main(id,request):
    import datetime
    Task = Tasks.query.order_by(Tasks.time_create.desc())
    tasks_schema = TasksSchema(many=True)
    resp=tasks_schema.dump(Task)
    return resp


def delete(id):
    task = db.session.query(Tasks).filter_by(task_id=int(id)).one()
    db.session.delete(task)
    db.session.commit()
    return {"deleted":id}

def add(request):
    arra = json.dumps(request)
    arra = json.loads(arra)
    try:
        task_id = db.session.query(Tasks.task_id).order_by(Tasks.task_id.desc()).first()[0] + 1
    except:
        task_id = 1
    date = datetime.now()
    if arra['taskName']!='':
        task = Tasks (
            task_id = task_id,
            task_name = arra['taskName'],
            time_create = str(date),
            status = '1'
        )
        try:
            db.session.add(task)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logger.info(" ------- add request rollback ------- {}".format(e))
        return 1
    else:
        return 0
