from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class CategoryForm(FlaskForm):
    pass

class ProductForm(FlaskForm):
    pass

class checkoutForm(FlaskForm):
    pass