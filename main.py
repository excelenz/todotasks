# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_app]
# [START gae_python3_app]
import datetime
import logging
import os
from flask import Flask, render_template, request, Response, jsonify
from flask import Blueprint
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
import secret

db_user = secret.db_user
db_pass = secret.db_pass
db_name = secret.db_name
db_host = secret.db_host
db_socket_dir = secret.db_socket_dir
cloud_sql_connection_name = secret.cloud_sql_connection_name


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)
logger = logging.getLogger()

def create_app(config_filename):
    app.config.from_object(config_filename)
    api_bp = Blueprint('api', __name__)
    api = Api(api_bp)
    db = SQLAlchemy(app)
    from models import Tasks
    db.init_app(app)
    return app



def init_connection_engine():
    db_config = {
        # [START cloud_sql_mysql_sqlalchemy_limit]
        # Pool size is the maximum number of permanent connections to keep.
        "pool_size": 5,
        # Temporarily exceeds the set pool_size if no connections are available.
        "max_overflow": 2,

        # [END cloud_sql_mysql_sqlalchemy_limit]

        # [START cloud_sql_mysql_sqlalchemy_backoff]

        # [END cloud_sql_mysql_sqlalchemy_backoff]

        # [START cloud_sql_mysql_sqlalchemy_timeout]
        "pool_timeout": 30,  # 30 seconds
        # [END cloud_sql_mysql_sqlalchemy_timeout]

        # [START cloud_sql_mysql_sqlalchemy_lifetime]
        "pool_recycle": 1800,  # 30 minutes
        # [END cloud_sql_mysql_sqlalchemy_lifetime]
    }
    return init_unix_connection_engine(db_config)


def init_unix_connection_engine(db_config):
    # [START cloud_sql_mysql_sqlalchemy_create_tcp]
    host_args = db_host.split(":")
    db_hostname, db_port = host_args[0], int(host_args[1])
    pool = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL(
            drivername="mysql+pymysql",
            username=db_user,
            password=db_pass,
            host=db_hostname,
            port=db_port,
            database=db_name,
        ),
        **db_config
    )
    # [END cloud_sql_mysql_sqlalchemy_create_tcp]
    return pool
db = None

#@app.before_first_request
def create_tables():
    global db
    db = db or init_connection_engine()
    # Create tables (if they don't already exist)
    with db.connect() as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS tasks "
            "( task_id  SERIAL NOT NULL, time_create  CHAR(255), "
            "task_name  CHAR(255) NOT NULL,status INT, PRIMARY KEY (task_id) );"
        )


@app.route('/')
def hello():
    """Return I'alive HTTP greeting."""
    message = "TO DO TASK LISK // \xA9 Dmitry Margolin"
    return render_template('index.html',message = message)

@app.route('/api/tasks/add/',methods=['GET','POST'])
def tasksListAdd():
    import tasks
    resp=tasks.add(request.get_json())
    return jsonify(resp)

@app.route('/api/tasks/delete/<id>/',methods=['DELETE'])
def tasksListDelete(id):
    import tasks
    resp=tasks.delete(id)
    return jsonify(resp)

@app.route('/api/tasks/<id>/', defaults={'id':0},methods=['PUT','POST'])
@app.route('/api/tasks/', defaults={'id':0},methods=['GET','POST'])
def tasksList(id):
    import tasks
    resp=tasks.main(id,request.get_json())
    return jsonify(resp)

app = create_app("config")
if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8020, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]
