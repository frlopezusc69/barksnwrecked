from . import bp as main
from flask import render_template
from .models import Product, Category, Cart, Order, SaleTransaction
from app.blueprints.auth.models import User

@main.route('/', methods=['GET'])
@main.route('/home')
def home():
    return render_template('index.html', home=home)
        
@main.route('/displayCategory')
def displayCategory():
   pass 
@main.route('/productDescription')
def productDescrption():
    pass
@main.route("/addtoCart")
def addtoCart():
    pass
@main.route("/cart")
def cart():
    pass
@main.route('/category')
def category():
    pass
@main.route('/updatecategory')
def update_category():
    pass
@main.route('/deletecategory')
def delete_category():
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
    pass
@main.route('/createorder', methods=['GET', 'POST'])
def createOrder():
    pass