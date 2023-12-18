from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controllers.homes_controller import homes_controller

app = Flask(__name__)
app.config.from_object('ItemFinder.config')

db = SQLAlchemy(app)

app.register_blueprint(homes_controller, url_prefix="/")

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5001, debug=True)