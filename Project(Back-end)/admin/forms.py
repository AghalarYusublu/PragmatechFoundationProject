from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FileField,TextAreaField



class MenuForm(FlaskForm):
    link_name=StringField('link_name')
    submit=SubmitField()

class BannerForm(FlaskForm):
    b_title=StringField('b_title')
    b_subtitle=StringField('b_subtitle')
    b_txt=StringField('b_txt')
    b_postitle=StringField('b_postitle')
    b_img=FileField('b_img')
    submit=SubmitField()


class FeaturesForm(FlaskForm):
    f_icon=StringField('f_icon')
    f_title=StringField('f_title')
    f_text=StringField('f_text')
    submit=SubmitField()

  
class FoodpackageForm(FlaskForm):
   package=StringField('package')
   submit=SubmitField()

class AboutForm(FlaskForm):
    about_chef_name=StringField('about_chef_name')
    about_title=StringField('about_title')
    about_txt=StringField('about_txt')
    about_img=FileField('about_img')
    submit=SubmitField()

class AboutDetailsForm(FlaskForm):
    about_details=StringField('about_details')
    submit=SubmitField()

class ProductForm(FlaskForm):
    p_name=StringField('p_name')
    p_price=StringField('p_price')
    p_txt=StringField('p_txt')
    p_menu_pdf_url=StringField('p_menu_pdf_url')
    product_img=FileField('product_img')
    submit=SubmitField()


class TestimonialsForm(FlaskForm):
    clinet_name=StringField('clinet_name')
    client_testimonial=TextAreaField('client_testimonial')
    client_img=FileField('client_img')
    submit=SubmitField()


class ContactForm(FlaskForm):
    contact_phone=StringField('contact_phone')
    contact_email=StringField('contact_email')
    contact_location=StringField('contact_location')
    submit=SubmitField()



class SocialLinksForm(FlaskForm):
    s_icon=StringField('s_icon')
    s_icon_url=StringField('s_icon_url')
    submit=SubmitField()



    