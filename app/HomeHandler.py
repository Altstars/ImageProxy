
from app.BaseHandler import BaseHandler
from models.model import *

class HomeHandler(BaseHandler):
  def get(self):
    self.render("index.html")

