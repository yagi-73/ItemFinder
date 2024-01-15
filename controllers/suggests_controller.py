from flask import Blueprint, render_template, request
from models.item import Item
from moore_AI_test.AI_test import st_search

suggests_controller = Blueprint("suggests_controller", __name__)

@suggests_controller.route("capture")
def capture():
  return render_template("suggests/capture.html")

@suggests_controller.route("analyze", methods=["POST"])
def analyze():
  image = request.files['image']
  img_path = '/Users/moore/git/ItemFinder/moore_AI_test/sanple_image/61obz82MvTL._AC_UF894,1000_QL80_.jpg'
  shirts = Item.query.filter_by(genre_id=1).all()
  jacket = Item.query.filter_by(genre_id=2).all()
  pants = Item.query.filter_by(genre_id=3).all()
  result = st_search(img_path)
  items = [shirts[result[0]], jacket[result[1]], pants[result[2]]]
  return render_template("suggests/result.html", items = items)


@suggests_controller.route("result")
def result():
  items = Item.query.all()
  return render_template("suggests/result.html", items = items)