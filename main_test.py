# Copyright 2018 Google Inc. All Rights Reserved.
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

import main
import pytest
from models import Tasks


def test_index():
    main.app.testing = True
    client = main.app.test_client()
    r = client.get('/')
    assert r.status_code == 200
    assert 'TO DO LIST' in r.data.decode('utf-8')


@pytest.fixture(scope='module')
def new_task():
    task = Tasks('1111111','Task 1 test','1617817587')
    return task


def test_create_new_task(new_task):
    assert new_task.task_name == 'Task 1 test'
    assert new_task.time_create == '1617817587'
    assert new_task.status == '1'
