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
      
      ## jacket
      Item(genre_id = 1, name='タートルネックセーター', price=5000, image_url='/static/images/jacket/jacket_img1.jpg', display_area_x=10, display_area_y=5),
      Item(genre_id = 1, name='エレガンスコート', price=12000, image_url='/static/images/jacket/jacket_img2.jpg', display_area_x=74, display_area_y=7),
      Item(genre_id = 1, name='レザージャケット', price=18000, image_url='/static/images/jacket/jacket_img3.jpg', display_area_x=91, display_area_y=32),
      Item(genre_id = 1, name='シルエットパーカー', price=6500, image_url='/static/images/jacket/jacket_img4.jpg', display_area_x=91, display_area_y=80),
      Item(genre_id = 1, name='ニットセーター', price=7000, image_url='/static/images/jacket/jacket_img5.jpeg', display_area_x=30, display_area_y=91),
      
      ## pants
      Item(genre_id = 2, name='デニムショーツ', price=3800, image_url='/static/images/pants/pants_img1.jpg', display_area_x=2, display_area_y=15),
      Item(genre_id = 2, name='スキニーレギンス', price=4500, image_url='/static/images/pants/pants_img2.jpg', display_area_x=5, display_area_y=37),
      Item(genre_id = 2, name='クラシックパンツ', price=5800, image_url='/static/images/pants/pants_img3.jpg', display_area_x=2, display_area_y=53),
      Item(genre_id = 2, name='スキニージーンズ', price=5500, image_url='/static/images/pants/pants_img4.jpg', display_area_x=5, display_area_y=65),
      Item(genre_id = 2, name='スキニーパンツ', price=6500, image_url='/static/images/pants/pants_img5.jpg', display_area_x=3, display_area_y=78),
      
      ## shirt
      Item(genre_id = 3, name='コットンTシャツ', price=2800, image_url='/static/images/shirt/shirt_img1.jpeg', display_area_x=25, display_area_y=33),
      Item(genre_id = 3, name='プリントTシャツ', price=2500, image_url='/static/images/shirt/shirt_img2.jpeg', display_area_x=40, display_area_y=40),
      Item(genre_id = 3, name='クルーネックTシャツ', price=2600, image_url='/static/images/shirt/shirt_img3.jpeg', display_area_x=30, display_area_y=67),
      Item(genre_id = 3, name='ロングスリーブTシャツ', price=3000, image_url='/static/images/shirt/shirt_img4.jpeg', display_area_x=58, display_area_y=35),
      Item(genre_id = 3, name='グラフィックTシャツ', price=3500, image_url='/static/images/shirt/shirt_img5.jpeg', display_area_x=70, display_area_y=72),
    ]

    db.session.add_all(items)
    db.session.commit()

if __name__ == '__main__':
  genre_seed()
  item_seed()