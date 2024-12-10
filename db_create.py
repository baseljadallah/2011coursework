from app import db, create_app
from app.models import Product, Category, Tag

app = create_app()
with app.app_context():

    db.create_all()

    # Categories
    bw_puffers = Category(name='Puffers')
    bw_tshirts = Category(name='T-Shirts')
    bw_hoodies = Category(name='Hoodies')
    bw_sweatpants = Category(name='Sweatpants')
    b_zippers = Category(name='Zipper Jackets')

    # Adding products
    p1 = Product(name='black puffer', price='$120', img='images/black-puffer.png', alt='Made with LOVE. 100% Polyster', stock=10, category=bw_puffers)
    p2 = Product(name='cream puffer', price='$120', img='images/cream-puffer.png', alt='Made with LOVE. 100% Polyster', stock=5, category=bw_puffers)
    p3 = Product(name='white tshirt', price='$45', img='images/white-tshirt.png', alt='Made with LOVE. 100% Cotton', stock=10, category=bw_tshirts)
    p4 = Product(name='black tshirt', price='$45', img='images/black-tshirt.png', alt='Made with LOVE. 100% Cotton', stock=0, category=bw_tshirts)
    p5 = Product(name='black hoodie', price='$80', img='images/black-hoodie.png', alt='Made with LOVE. 100% Cotton', stock=10, category=bw_hoodies)
    p6 = Product(name='grey hoodie', price='$80', img='images/grey-hoodie.png', alt='Made with LOVE. 100% Cotton', stock=10, category=bw_hoodies)
    p7 = Product(name='black sweatpants', price='$60', img='images/black-pants.png', alt='Made with LOVE. 100% Cotton', stock=10, category=bw_sweatpants)
    p8 = Product(name='grey sweatpants', price='$60', img='images/grey-pants.png', alt='Made with LOVE. 100% Cotton', stock=10, category=bw_sweatpants)
    p9 = Product(name='black zipper', price='$85', img='images/zipper-jacket.png', alt='Made Normally. 100% Cotton', stock=10, category=b_zippers)

    #tags
    poly_tag = Tag(name="Polyster")
    cotton_tag = Tag(name="Cotton")

    # Commiting
    db.session.add_all([bw_puffers ,bw_tshirts, bw_hoodies, bw_sweatpants, b_zippers])
    db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8, p9])
    db.session.add(poly_tag)
    db.session.add(cotton_tag)
    db.session.commit()
 
    #assigning 
    products = Product.query.order_by(Product.id).all()
    if len(products) >= 1:
        products[0].tags.append(poly_tag) # black puffer
    if len(products) >= 2:
        products[1].tags.append(poly_tag) # cream  puffer
    if len(products) >= 3:
        products[2].tags.append(cotton_tag) # black tshirt
    if len(products) >= 4:
        products[3].tags.append(cotton_tag) # white tshirt
    if len(products) >= 5:
        products[4].tags.append(cotton_tag) # black hoodie
    if len(products) >= 6:
        products[5].tags.append(cotton_tag) # grey hoodie
    if len(products) >= 7:
        products[6].tags.append(cotton_tag) # black sweatpants
    if len(products) >= 8:
        products[7].tags.append(cotton_tag) # grey sweatpants
    if len(products) >= 9:
        products[8].tags.append(cotton_tag) # black zipper

    db.session.commit()
