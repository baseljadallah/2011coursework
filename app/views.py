from flask import Blueprint, render_template, request, redirect, url_for, session
from app import db
from app.models import Product
from flask_login import login_required, current_user
from flask_admin.contrib.sqla import ModelView

views = Blueprint('views', __name__)


@views.route('/')
@login_required  # must be logged in to access
def home():
    return render_template("home.html", user=current_user)

@views.route('/products')
def page1():
    products = Product.query.all()
    return render_template("products.html", user=current_user, products= products)

@views.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get(product_id)
    return render_template('product_detail.html', user=current_user, product=product)

@views.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = request.form.get('product_id')
    size = request.form.get('size')

    product = Product.query.get(product_id)
    if product.stock <= 0:
        return "This product is out of stock."
    
    # removes stock when added to cart
    product.stock -= 1
    db.session.commit()

    #adds products to the cart
    session['cart'].append({
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'img': product.img,
        'size': size})
    
    session.modified = True

    return redirect(url_for('views.cart'))

@views.route('/cart')
@login_required
def cart():
    cart_items = session.get('cart', [])
    return render_template('cart.html', user=current_user, cart_items=cart_items)

@views.route('/remove_from_cart/<int:product_id>', methods=['GET', 'POST'])
def remove_from_cart(product_id):
    cart_items = session.get('cart', [])
    # finds the item in the cart
    item_index = None
    for i, item in enumerate(cart_items):
        if item['id'] == product_id:
            item_index = i
            break

    if item_index is not None:
        # put the item back in stock when the user removes it from the cart
        product = Product.query.get(product_id)
        if product:
            product.stock += 1
            db.session.commit()

        #removes product from the cart
        cart_items.pop(item_index)
        session['cart'] = cart_items
        session.modified = True

    return redirect(url_for('views.cart'))

@views.route('/wishlist')
@login_required
def wishlist():
    wishlist_items = session.get('wishlist', [])
    return render_template('wishlist.html', user=current_user, wishlist_items=wishlist_items)
