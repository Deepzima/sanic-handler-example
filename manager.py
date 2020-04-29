import os
from sanic_script import Manager
from server import create_app

app = create_app(os.getenv("FLASK_ENV") or "dev")

manager = Manager(app)
# app.app_context().push()

@manager.command
def run():
    app.run(host=app.config['HOST'],
            port=app.config['PORT'],
            debug=app.config['DEBUG'])


if __name__ == "__main__":
    manager.run()
