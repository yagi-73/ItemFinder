from flask import Blueprint, render_template
from models.item import Item
homes_controller = Blueprint("homes_controller", __name__)

@homes_controller.route("/")
def top():
  return render_template("homes/top.html")