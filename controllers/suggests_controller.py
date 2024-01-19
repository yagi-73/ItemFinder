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
  # img_path = 'C:/Users/souta_aoyagi/workspace/ItemFinder/moore_AI_test/sanple_image/tensinmukai.jpeg'
  recommended_feature = st_search(image)
  shirts = Item.query.filter_by(genre_id = 1, feature=recommended_feature.shirts).first()
  jacket = Item.query.filter_by(genre_id = 2, feature=recommended_feature.jacket).first()
  pants = Item.query.filter_by(genre_id = 3, feature=recommended_feature.pants).first()
  items = [shirts, jacket, pants]
  return render_template("suggests/result.html", items = items)


@suggests_controller.route("result")
def result():
  items = Item.query.limit(3).all()
  return render_template("suggests/result.html", items=items)
