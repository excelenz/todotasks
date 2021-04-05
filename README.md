# todotasks



run local:
  source env/bin/activate
  export PATH=$PATH:/usr/local/mysql/bin/
  sudo mysql -p
  gcloud sql connect todolist --user=root


  python3 -m pip install mysql-connector-python
