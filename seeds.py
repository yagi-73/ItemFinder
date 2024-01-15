from app import app, db
from models.item import Item
from models.genre import Genre

def genre_seed():
  with app.app_context():
    genres = [
      Genre(name='jacket'),
      Genre(name='pants'),
      Genre(name='shirts'),
    ]
  
    db.session.add_all(genres)
    db.session.commit()

def item_seed():
  with app.app_context():
    items = [
      # Item(name='クルーネックTシャツ(緑)', price=990, image_url='/static/images/clothes-g1f027b564_640.jpg', display_area_x=20, display_area_y=10),
      # Item(name='スウェット(白)', price=2900, image_url='/static/images/img2.png', display_area_x=60, display_area_y=87),
      # Item(name='ニットポンチョ(白)', price=5900, image_url='/static/images/img3.png', display_area_x=7, display_area_y=20),
      # Item(name='ハイウエストパンツ(ピンク)', price=5800, image_url='/static/images/img4.png', display_area_x=75, display_area_y=10),
      
      ## jacket
      Item(genre_id = 1, name='タートルネックセーター', price=5000, image_url='/static/images/jacket/jacket_img1.jpg', display_area_x=5, display_area_y=10),
      Item(genre_id = 1, name='エレガンスコート', price=12000, image_url='/static/images/jacket/jacket_img2.jpg', display_area_x=90, display_area_y=20),
      Item(genre_id = 1, name='レザージャケット', price=18000, image_url='/static/images/jacket/jacket_img3.jpg', display_area_x=5, display_area_y=38),
      Item(genre_id = 1, name='シルエットパーカー', price=6500, image_url='/static/images/jacket/jacket_img4.jpg', display_area_x=7, display_area_y=53),
      Item(genre_id = 1, name='ニットセーター', price=7000, image_url='/static/images/jacket/jacket_img5.jpeg', display_area_x=5, display_area_y=74),
      
      ## pants
      Item(genre_id = 2, name='デニムショーツ', price=3800, image_url='/static/images/pants/pants_img1.jpg', display_area_x=75, display_area_y=10),
      Item(genre_id = 2, name='スキニーレギンス', price=4500, image_url='/static/images/pants/pants_img2.jpg', display_area_x=75, display_area_y=10),
      Item(genre_id = 2, name='クラシックパンツ', price=5800, image_url='/static/images/pants/pants_img3.jpg', display_area_x=75, display_area_y=10),
      Item(genre_id = 2, name='スキニージーンズ', price=5500, image_url='/static/images/pants/pants_img4.jpg', display_area_x=75, display_area_y=10),
      Item(genre_id = 2, name='スキニーパンツ', price=6500, image_url='/static/images/pants/pants_img5.jpg', display_area_x=75, display_area_y=10),
      
      ## shirt
      Item(genre_id = 3, name='コットンTシャツ', price=2800, image_url='/static/images/shirt/shirt_img1.jpeg', display_area_x=75, display_area_y=10),
      Item(genre_id = 3, name='プリントTシャツ', price=2500, image_url='/static/images/shirt/shirt_img2.jpeg', display_area_x=75, display_area_y=10),
      Item(genre_id = 3, name='クルーネックTシャツ', price=2600, image_url='/static/images/shirt/shirt_img3.jpeg', display_area_x=75, display_area_y=10),
      Item(genre_id = 3, name='ロングスリーブTシャツ', price=3000, image_url='/static/images/shirt/shirt_img4.jpeg', display_area_x=75, display_area_y=10),
      Item(genre_id = 3, name='グラフィックTシャツ', price=3500, image_url='/static/images/shirt/shirt_img5.jpeg', display_area_x=75, display_area_y=10),
    ]

    db.session.add_all(items)
    db.session.commit()

if __name__ == '__main__':
  genre_seed()
  item_seed()