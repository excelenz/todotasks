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
from flask import Flask, render_template, request, Response
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint
from flask_restful import Api


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



@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

app = create_app("config")
if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]
