from app import app, db
from models.item import Item

def item_seed():
  with app.app_context():
    items = [
      Item(name='クルーネックTシャツ(緑)', price=990, image_url='/static/images/img1.png'),
      Item(name='スウェット(白)', price=2900, image_url='/static/images/img2.png'),
      Item(name='ニットポンチョ(白)', price=5900, image_url='/static/images/img3.png'),
      Item(name='ハイウエストパンツ(ピンク)', price=5800, image_url='/static/images/img4.png'),
    ]

    db.session.add_all(items)
    db.session.commit()

if __name__ == '__main__':
  item_seed()