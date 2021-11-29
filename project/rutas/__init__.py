from flask import Blueprint


routes = Blueprint('routes', __name__)

from App import mysql
from .index import *
from .rutasbd import usuario
from .rutasbd import rol
