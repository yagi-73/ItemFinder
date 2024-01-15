from flask import Flask
from database import db
from models import *
from flask_migrate import Migrate
from controllers.homes_controller import homes_controller
from controllers.suggests_controller import suggests_controller

app = Flask(__name__)
app.config.from_pyfile('config.py')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(homes_controller, url_prefix="/")
app.register_blueprint(suggests_controller, url_prefix="/suggests")

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5001, debug=True)