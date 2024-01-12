from flask import Blueprint, render_template
homes_controller = Blueprint("homes_controller", __name__)

@homes_controller.route("/")
def top():
  return render_template("top.html")

@homes_controller.route("last_page")
def itemFinder():
  return render_template("last_page.html")