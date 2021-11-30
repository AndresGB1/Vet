from flask import Blueprint


from .. import mysql
from .. import routes

from .usuario.rol import *
from .usuario.user import *