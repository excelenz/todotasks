# todotasks

run local:
  git clone https://github.com/excelenz/todotasks.git
  source env/bin/activate
  (you should install it https://cloud.google.com/python/docs/getting-started?hl=en_GB)
  python3 main.py

deploying to cloud:
  gcloud app deploy

When you first run locally change the path to DB in config.py to
uncomment #@app.before_first_request in main.py

It will connect remotely to MYSQL db in google cloud.
this file should be secret (in this project it's just a file) secret.py - put there your credentials to cloud db
you should update app.yaml (the reason there are two file - I developed all in sqlight and then move db to cloud)
you should allow your ip on google cloud
you need cloud sql admin role to the cloud function service account
you need to declare environment variables  in app.yaml


  usefull:
  gcloud sql connect todolist --user=root
  gcloud app logs tail -s default
