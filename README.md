# todotasks

run local:
  git clone https://github.com/excelenz/todotasks.git
  source env/bin/activate (you should install it https://cloud.google.com/python/docs/getting-started?hl=en_GB)
  python3 main.py

deploying to cloud:
  gcloud app deploy

When you firt run locally change the path to DB in config.py to
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}/{}".format(db_user,db_pass,db_host,db_name)

It will connect remotely to db in google cloud. Install all what you need.
Then change it back and deploy. There is some problem with environment variables that they suggest to use
(if os.environ.get("DB_HOST"):) so you cannot use their manuals https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/cloud-sql/mysql/sqlalchemy/main.py
also: https://filipmolcik.com/cant-connect-to-mysql-server-on-localhost-google-sql/
you should allow your ip on google cloud



  usefull:
  gcloud sql connect todolist --user=root
  gcloud app logs tail -s default
