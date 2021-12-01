from flask import Blueprint


from .. import mysql
from .. import routes

from .usuarior.rol import *
from .usuarior.user import *
from .mascotar.mascota import *