from . import bp as main
from flask_session import Session
from flask import Flask, render_template, redirect, request, session, flash, url_for
from .models import Product, Category, Cart, Order, SaleTransaction
from app.blueprints.auth.models import User
from .forms import checkoutForm

@main.route('/', methods=['GET'])
@main.route('/home')
def home():
    product = product.query.all()
    return render_template('index.html', products=products)
    # items = db.execute("SELECT * FROM products ORDER BY name")
    # itemsLen = len(items)
    # shopping_cart = []
    # shopLen = len(shopping_cart)
    # totItems, total, display = 0, 0, 0
    # if User in session:
    #     shopping_cart = db.execute("SELECT product_name, image, quantity, price FROM products")
    #     shopLen=len(shopping_cart)
    #     for i in range(shopLen):
    #         total += shoppingCart[i]["SUM(price)"]
    #         totItems += shoppingCart[i]["SUM(quantity)"]
    #     items = db.execute("SELECT * FROM products ORDER BY name")
    
        
@main.route('/productDescription')
def productDescrption():
    productdetails = product.query.filter(product_id)
    return render_template('product.html', data = productdetails, product=product)
@main.route("/addtoCart")
def addtoCart():
    User = User.query.filter_by(username=username).first()
    if User is None or not:
        return redirect(url_for('auth.login'))
    else:
        flash("Item successfully added to cart!!", "success")
        return redirect(url_for('main.index'))
    
@main.route("/cart")
def cart():
    User = User.query.filter_by(username=username).first()
    if User in session:
        totItems, total, display = 0,0,0
        shoppingCart = db.execute("SELECT product_name, image, quantity, price From products")
        shopLen = len(shoppingCart)
        for i in range(shopLen):
            total += shoppingCart[i]["SUM(total"]
    return render_template('cart.html', **context, home=home)
    else:
        return redirect(url_for('auth.login'))
@main.route('/category')
def category():
    pass
@main.route('/products')
def product(product_id):
    pass
@main.route('/users')
def getUsers():
    pass
@main.route('/removefromCart')
def removeFromCart():
    pass
@main.route('/checkoutPage')
def checkoutForm():
    order = db.execute("Select * from cart")
    for item in order:
        db.execute("INSERt INTO purchases ")
@main.route('/createorder', methods=['GET', 'POST'])
def createOrder():
    pass