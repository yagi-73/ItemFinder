from datetime import datetime
import pytz
from database import db

class Genre(db.Model):
  __tablename__ = 'genres'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(30), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone("Asia/Tokyo")))
