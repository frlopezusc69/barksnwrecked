from flask import Blueprint
from datetime import datetime

bp = Blueprint('main', __name__)

from . import routes, models