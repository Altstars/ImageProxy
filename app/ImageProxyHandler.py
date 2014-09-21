
from app.BaseHandler import BaseHandler
from models.model import *
import urllib.request
import os.path
import hashlib

from PIL import Image

class ImageProxyHandler(BaseHandler):
  def get(self, width, height):
    if width is None or height is None:
      width = height = 0
    width = int(width)
    height = int(height)

    url = self.get_argument("url")
    
    image_path = self._get_image(url, width, height)

    with open(image_path, "rb") as f:
      data = f.read()
      self.set_header('Content-type', "image/jpeg" + self._get_ext(image_path)[1][1:])
      self.set_header('Content-length', len(data))
      self.write(data)
 
  def _get_image(self, url, width, height):
    image_path = self._to_image_path(url)
    self._fetch_image(url, image_path)

    if not (width == 0 or height == 0):
      image_path = self._get_thumbnail(image_path, width, height)

    return image_path

  def _get_thumbnail(self, original_image_path, width, height):
    suffix = ".{}x{}".format(width,height)
    thumb_image_path = suffix.join(os.path.splitext(original_image_path))
    if not os.path.exists(thumb_image_path):
      image = Image.open(original_image_path)
      image.thumbnail((width, height), Image.ANTIALIAS)
      image.save(thumb_image_path)
    return thumb_image_path


  def _fetch_image(self, url, image_path):
    
    if not os.path.exists(image_path):
      image_url = urllib.request.urlopen(url)
      image = image_url.read()
      f = open(image_path, "wb")
      f.write(image)
      f.close()

  def _to_image_path(self, url):
    return "images/originals/" + hashlib.sha256(url.encode("utf-8")).hexdigest() + self._get_ext(url)

  def _get_ext(self, path):
    return os.path.splitext(path)[1]


  def _search_image_by_cache(self,url):
    pass



