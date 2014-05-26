
from app.BaseHandler import BaseHandler

# CAUTION 完全未実装
class AuthLoginHandler(BaseHandler):
  def get(self):
    self.render("auth/login.html")

  def post(self):
    #TODO SIGN IN
    self.set_secure_cookie("user","Kouki Saito")
    self.redirect("/"+str(status))

class AuthLogoutHandler(BaseHandler):
  def get(self):
    self.render("auth/logout.html")

