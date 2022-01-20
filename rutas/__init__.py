from flask import Blueprint


routes = Blueprint('routes', __name__,template_folder='templates')

from .index import *
from .rutasbd.__init__ import *

