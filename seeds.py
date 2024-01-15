from app import app, db
from models.item import Item

def item_seed():
  with app.app_context():
    items = [
      Item(name='クルーネックTシャツ(緑)', price=990, image_url='/static/images/img1.png', display_area_x=20, display_area_y=10),
      Item(name='スウェット(白)', price=2900, image_url='/static/images/img2.png', display_area_x=60, display_area_y=87),
      Item(name='ニットポンチョ(白)', price=5900, image_url='/static/images/img3.png', display_area_x=7, display_area_y=20),
      Item(name='ハイウエストパンツ(ピンク)', price=5800, image_url='/static/images/img4.png', display_area_x=75, display_area_y=10),
    ]

    db.session.add_all(items)
    db.session.commit()

if __name__ == '__main__':
  item_seed()