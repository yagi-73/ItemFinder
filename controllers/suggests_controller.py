from flask import Blueprint, render_template
from models.item import Item
suggests_controller = Blueprint("suggests_controller", __name__)

@suggests_controller.route("result")
def result():
  items = Item.query.all()
  return render_template("suggests/result.html", items = items)