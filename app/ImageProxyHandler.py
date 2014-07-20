
from app.BaseHandler import BaseHandler
from models.model import *
import urllib.request

class ImageProxyHandler(BaseHandler):
  def get(self):
    url = self.get_argument("url")
    
    image = self._get_image(url)
    self.set_header('Content-type', image["content-type"])
    self.set_header('Content-length', len(image["data"]))
    self.write(image["data"])
 
    self.render("index.html")
  def _get_image(self, url):
    image_url = urllib.request.urlopen(url)
    content_type = image_url.info().get("content-type")
    image = image_url.read()

    return {
        "content-type":content_type,
        "data":image,
    }



