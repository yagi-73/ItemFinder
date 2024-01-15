from flask import Blueprint, render_template, request
import os
from models.item import Item

suggests_controller = Blueprint("suggests_controller", __name__)

@suggests_controller.route("capture")
def capture():
  return render_template("suggests/capture.html")

@suggests_controller.route("analyze", methods=["POST"])
def analyze():
  image = request.files['image']

@suggests_controller.route("result")
def result():
  items = Item.query.all()
  return render_template("suggests/result.html", items = items)