from app import db
from flask_login import UserMixin

# table that links the products and tags
product_tags = db.Table('product_tags',
    db.Column('product_id', db.Integer, db.ForeignKey('Product.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('Tag.id'), primary_key=True)
)

#information about users (email,password ect.)
class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50))
    first_name = db.Column(db.String(50))

class Category(db.Model):
    __tablename__ = 'Category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    products = db.relationship('Product', backref='category')

# product information and details
class Product(db.Model):
    __tablename__ = 'Product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.String, nullable=False)
    img = db.Column(db.String)
    alt = db.Column(db.String)
    stock = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('Category.id'), nullable=True)

    tags = db.relationship('Tag', secondary=product_tags, back_populates='products')

class Tag(db.Model):
    __tablename__ = 'Tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    products = db.relationship('Product', secondary=product_tags, back_populates='tags')
