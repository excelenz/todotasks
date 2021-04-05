from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models import db
from echobot import create_app

app = create_app('config')

migrate = Migrate(app, db)
migrate.init_app(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    manager.run()
    db.create_all()
    db.session.commit()
