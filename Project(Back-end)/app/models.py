from app import db   

class Menu(db.Model):
   id=db.Column(db.Integer,primary_key=True)
   nav_logo=db.Column(db.String(200))
   link_name=db.Column(db.String(150))
   
class Banner(db.Model):
   id=db.Column(db.Integer,primary_key=True)
   b_title=db.Column(db.String(70))
   b_subtitle=db.Column(db.String(150))
   b_txt=db.Column(db.String(200))
   b_postitle=db.Column(db.String(50))
   b_img=db.Column(db.String(200))

class Foodpackage(db.Model):
   id=db.Column(db.Integer,primary_key=True)
   package=db.Column(db.String(70))
   orders=db.relationship('Orders',backref='foodpackage',lazy=True)

class Orders(db.Model):
   id=db.Column(db.Integer,primary_key=True)
   package_name=db.Column(db.String(70))
   email=db.Column(db.String(200))
   phone=db.Column(db.String(150))
   comment=db.Column(db.String(250))
   complete_order_btn=db.Column(db.String(200))
   foodpackage_id=db.Column(db.Integer, db.ForeignKey('foodpackage.id'), nullable=False)

class About(db.Model):
   id=db.Column(db.Integer,primary_key=True)
   about_chef_name=db.Column(db.String(100))
   about_title=db.Column(db.String(200))
   about_txt=db.Column(db.String(200))
   about_img=db.Column(db.String(200))

class AboutDetails(db.Model):
   id=db.Column(db.Integer,primary_key=True)
   about_details=db.Column(db.String(250))

class Product(db.Model):
   id=db.Column(db.Integer,primary_key=True)
   p_name=db.Column(db.String(100))
   p_price=db.Column(db.String(50))
   p_txt=db.Column(db.String(250))
   p_menu_pdf_url=db.Column(db.String(200))
   product_img=db.Column(db.String(200))
   

class Testimonials(db.Model):
   id=db.Column(db.Integer,primary_key=True)
   clinet_name=db.Column(db.String(100))
   client_testimonial=db.Column(db.String(250))
   client_img=db.Column(db.String(250))

class Contact(db.Model):
   id=db.Column(db.Integer,primary_key=True)
   contact_phone=db.Column(db.String(150))
   contact_email=db.Column(db.String(250))
   contact_location=db.Column(db.String(250))

class SocialLinks(db.Model):
   id=db.Column(db.Integer,primary_key=True)
   s_icon=db.Column(db.String(150))
   s_icon_url=db.Column(db.String(150))
       

class Features(db.Model):
   id=db.Column(db.Integer,primary_key=True)
   f_icon=db.Column(db.String(150))
   f_title=db.Column(db.String(100))
   f_text=db.Column(db.String(200))

