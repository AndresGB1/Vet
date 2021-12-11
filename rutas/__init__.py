from flask import Blueprint


routes = Blueprint('routes', __name__,template_folder='templates')

from main import mysql
from .index import *
from .rutasbd.__init__ import *
