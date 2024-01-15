from datetime import datetime
import pytz
from database import db

class Item(db.Model):
  __tablename__ = 'items'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  genre_id = db.Column(db.Integer, nullable=False)
  name = db.Column(db.String(30), nullable=False)
  price = db.Column(db.Integer, nullable=False)
  display_area_x = db.Column(db.Integer, nullable=False)
  display_area_y = db.Column(db.Integer, nullable=False)
  image_url = db.Column(db.String(255))
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone("Asia/Tokyo")))