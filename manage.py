from flask.ext.script import Manager
import os

from programmerJobs import app, db
app.config.from_object(os.environ['APP_SETTINGS'])

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
