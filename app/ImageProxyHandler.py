
from app.BaseHandler import BaseHandler
from models.model import *

class ImageProxyHandler(BaseHandler):
  def get(self):
    url = self.get_argument("url")
    
    image = self._get_image(url)
    self.set_header('Content-type', 'image/png')
    self.set_header('Content-length', len(image))
    self.write(image)
 
    self.render("index.html")
  def _get_image(self,url):
    f = open("./images/sample.png","rb")
    return f.read()



