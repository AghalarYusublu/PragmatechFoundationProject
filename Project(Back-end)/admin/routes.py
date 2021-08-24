# admin routes
from app import app 
from app.models import *
import os
from admin.forms import *
from app import db
from flask import render_template,redirect,request,url_for
from werkzeug.utils import secure_filename
import itertools 



@app.route("/admin/")
def admin_index():
    return render_template('admin/dashboard.html')

@app.route("/")
def index():
    banner=Banner.query.all()
    about=About.query.all()
    features=Features.query.all()
    contact=Contact.query.all()
    social_link=SocialLinks.query.all()
    package=Foodpackage.query.all()
    orders=Orders.query.all()
    testimonials=Testimonials.query.all()
    product=Product.query.all()
    about_details=AboutDetails.query.all()
    menu=Menu.query.all()
    menuItem=["scrollPrograms(this)","scrollAbout(this)","scrollClients(this)"]
    menuID=["programs","about","clients"]
    newList=[]
    for i in range(len(menuItem)):
        newList.append({
            'menu': menu[i],
            'menuItem': menuItem[i],
            'menuID':menuID[i]
        })    
    return render_template('main/index.html',banner=banner,about=about,features=features,contact=contact,social_link=social_link,package=package,orders=orders,testimonials=testimonials,product=product,about_details=about_details,menu=menu,menuItem=menuItem,newList=newList)

@app.route("/admin/tables/")
def admin_tables():
    admin_banner=Banner.query.all()
    admin_about=About.query.all()
    admin_testimonial=Testimonials.query.all()
    admin_contact=Contact.query.all()
    admin_social_link=SocialLinks.query.all()
    admin_feature=Features.query.all()
    admin_food_package=Foodpackage.query.all()
    orders=Orders.query.all()
    admin_product=Product.query.all()
    admin_about_details=AboutDetails.query.all()
    admin_menu=Menu.query.all()
    return render_template('admin/tables.html',admin_banner=admin_banner, admin_about=admin_about, admin_testimonial=admin_testimonial, admin_contact=admin_contact,admin_social_link=admin_social_link,admin_feature=admin_feature,admin_food_package=admin_food_package,orders=orders,admin_product=admin_product,admin_about_details=admin_about_details,admin_menu=admin_menu)



@app.route('/admin/menu/',methods=['GET','POST'])
def admin_menu():
    menuItem=["scrollPrograms(this)","scrollAbout(this)","scrollClients(this)"]
    menuID=["programs","about","clients"]
    form=MenuForm()
    i=0
    while i<len(menuItem):
        i+=1
    j=0
    while j<len(menuID):
        j+=1
    if request.method=='POST':
        menu=Menu(
            link_name=form.link_name.data
        )
        db.session.add(menu)
        db.session.commit()     
        return redirect(url_for('admin_tables'))
    return render_template('admin/menu.html',form=form,menuItem=menuItem,menuID=menuID)

@app.route('/admin/menu-update/<id>',methods=['GET','POST'])
def admin_menu_update(id):
    menu=Menu.query.get(id)
    form=MenuForm()
    if request.method=='POST':
    
        menu.link_name=form.link_name.data
  
        db.session.commit()
        return redirect(url_for('admin_tables'))
    return render_template('admin/menu-update.html',form=form,menu=menu)

@app.route('/admin/menu/delete/<id>',methods=['GET','POST'])
def admin_menu_delete(id):
    menu=Menu.query.get(id)
    db.session.delete(menu)
    db.session.commit()
    return redirect(url_for('admin_tables'))
 
  
@app.route("/admin/banner/",methods=['GET','POSt'])
def admin_banner():  
    form=BannerForm()
    if request.method=='POST':
        file=form.b_img.data
        file_name=file.filename
        
        b_title = secure_filename(form.b_title.data)
        file_extention=file_name.split(".")[-1]
        newName=b_title+ '.' + file_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
        banner=Banner(
            b_title=form.b_title.data,
            b_subtitle=form.b_subtitle.data,
            b_txt=form.b_txt.data,
            b_postitle=form.b_postitle.data,
            b_img=newName
        )
        db.session.add(banner)
        db.session.commit()
        return redirect(url_for('admin_tables'))
    return render_template('admin/banner.html',form=form)

@app.route("/admin/banner-update/<id>",methods=['GET','POSt'])
def admin_banner_update(id):
    banner=Banner.query.get(id)
    form=BannerForm()
    if request.method=='POST':
        file=form.b_img.data
        file_name=file.filename        
        b_title = secure_filename(form.b_title.data)
        file_extention=file_name.split(".")[-1]
        newName=b_title+ '.' + file_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))

        banner.b_title=form.b_title.data
        banner.b_subtitle=form.b_subtitle.data
        banner.b_txt=form.b_txt.data
        banner.b_postitle=form.b_postitle.data
        banner.b_img=newName
        db.session.commit()
        return redirect(url_for('admin_tables'))
    return render_template('admin/banner-update.html',banner=banner,form=form)

@app.route('/admin/banner/delete/<id>',methods=['GET','POST'])
def admin_banner_delete(id):
    banner=Banner.query.get(id)
    db.session.delete(banner)
    db.session.commit()
    return redirect(url_for('admin_tables'))

@app.route("/admin/food-package/",methods=['GET','POST'])
def admin_food_package():
    form=FoodpackageForm()
    if request.method=='POST':
        package=Foodpackage(
            package=form.package.data
        )
        db.session.add(package)
        db.session.commit()
        return redirect(url_for('admin_tables'))
    return render_template('admin/food-package.html',form=form)


@app.route("/admin/food-package-update/<id>",methods=['GET','POST'])
def admin_food_package_update(id):
    package=Foodpackage.query.get(id)
    form=FoodpackageForm()
    if request.method=='POST':   
        package.package=form.package.data

        db.session.commit()
        return redirect(url_for('admin_tables'))
    return render_template('admin/food-package-update.html',package=package,form=form)

@app.route('/admin/food-package/delete/<id>',methods=['GET','POST'])
def admin_food_package_delete(id):
    package=Foodpackage.query.get(id)
    db.session.delete(package)
    db.session.commit()
    return redirect(url_for('admin_tables'))





@app.route("/admin/about/",methods=['GET','POST'])
def admin_about():
    form=AboutForm()
    if request.method=='POST':
        file=form.about_img.data
        file_name=file.filename 
        
        chef_name = secure_filename(form.about_chef_name.data)
        file_extention=file_name.split(".")[-1]
        newName=chef_name+ '.' + file_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
        about=About(
            about_chef_name=form.about_chef_name.data,
            about_title=form.about_title.data,
            about_txt=form.about_txt.data,
            about_img=newName
        )
        db.session.add(about)
        db.session.commit()
        return redirect(url_for('admin_tables'))
    return render_template('admin/about.html' , form=form)
    
@app.route("/admin/about-update/<id>",methods=['GET','POSt'])
def admin_about_update(id):
    about=About.query.get(id)
    form=AboutForm()
    if request.method=='POST':
        file=form.about_img.data
        file_name=file.filename 
        
        chef_name = secure_filename(form.about_chef_name.data)
        file_extention=file_name.split(".")[-1]
        newName=chef_name+ '.' + file_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
       
        about.about_chef_name=form.about_chef_name.data
        about.about_title=form.about_title.data
        about.about_txt=form.about_txt.data
        about.about_img=newName
        db.session.commit()
        return redirect(url_for('admin_tables'))
    return render_template('admin/about-update.html',about=about,form=form)
   
@app.route('/admin/about/delete/<id>',methods=['GET','POST'])
def admin_about_delete(id):
    about=About.query.get(id)
    db.session.delete(about)
    db.session.commit()
    return redirect(url_for('admin_tables'))
 
@app.route("/admin/about-details/",methods=['GET','POST'])
def admin_about_details():
    form=AboutDetailsForm()
    if request.method=='POST':
        about_details=AboutDetails(
            about_details=form.about_details.data
        )
        db.session.add(about_details)
        db.session.commit()
        return redirect(url_for('admin_tables'))
    return render_template('admin/about-details.html',form=form)   

@app.route("/admin/about-details-update/<id>",methods=['GET','POST'])
def admin_about_details_update(id):
    form=AboutDetailsForm()
    about_details=AboutDetails.query.get(id)
    if request.method=='POST':        
        about_details.about_details=form.about_details.data
        db.session.commit()
        return redirect(url_for('admin_tables'))
    return render_template('admin/about-details-update.html',about_details=about_details,form=form)   

@app.route('/admin/about-details/delete/<id>',methods=['GET','POST'])
def admin_about_details_delete(id):
    about_details=AboutDetails.query.get(id)
    db.session.delete(about_details)
    db.session.commit()
    return redirect(url_for('admin_tables'))
 


@app.route("/admin/product/",methods=['GET','POST'])
def admin_product():
    packages=Foodpackage.query.all()
    form=ProductForm()
    if request.method=='POST':
        file=form.product_img.data
        file_name=file.filename
        
        p_name = secure_filename(form.p_name.data)
        file_extention=file_name.split(".")[-1]
        newName=p_name+ '.' + file_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
        product=Product(
            p_name=form.p_name.data,
            p_price=form.p_price.data,
            p_txt=form.p_txt.data,
            p_menu_pdf_url=form.p_menu_pdf_url.data,
            product_img=newName
        )
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('admin_tables')) 
    return render_template('admin/product.html',packages=packages,form=form)

@app.route("/admin/product-update/<id>",methods=['GET','POST'])
def admin_product_update(id):
    product=Product.query.get(id)
    packages=Foodpackage.query.all()
    form=ProductForm()
    if request.method=='POST':
        file=form.product_img.data
        file_name=file.filename
        
        p_name = secure_filename(form.p_name.data)
        file_extention=file_name.split(".")[-1]
        newName=p_name+ '.' + file_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
    
        product.p_name=form.p_name.data
        product.p_price=form.p_price.data
        product.p_txt=form.p_txt.data
        product.p_menu_pdf_url=form.p_menu_pdf_url.data
        product.product_img=newName      
        db.session.commit()
        return redirect(url_for('admin_tables')) 
    return render_template('admin/product-update.html',packages=packages,product=product,form=form)


@app.route('/admin/product/delete/<id>',methods=['GET','POST'])
def admin_product_delete(id):
    product=Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('admin_tables'))
 
    

@app.route("/admin/testimonials/",methods=['GET','POST'])
def admin_testimonial():
    form=TestimonialsForm()
    if request.method=='POST':
        file=form.client_img.data
        file_name=file.filename
        
        clinet_name = secure_filename(form.clinet_name.data)
        file_extention=file_name.split(".")[-1]
        newName=clinet_name+ '.' + file_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))

        testimonials=Testimonials(
            clinet_name=form.clinet_name.data,
            client_testimonial=form.client_testimonial.data,
            client_img=newName
        )
        db.session.add(testimonials)
        db.session.commit()
        return redirect(url_for('admin_tables')) 

    return render_template('admin/testimonials.html',form=form)

@app.route("/admin/testimonials-update/<id>",methods=['GET','POST'])
def admin_testimonial_update(id):
    testimonial=Testimonials.query.get(id)
    form=TestimonialsForm()
    if request.method=='POST':
        file=form.client_img.data
        file_name=file.filename
        
        clinet_name = secure_filename(form.clinet_name.data)
        file_extention=file_name.split(".")[-1]
        newName=clinet_name+ '.' + file_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))

        testimonial.clinet_name=form.clinet_name.data
        testimonial.client_testimonial=form.client_testimonial.data
        testimonial.client_img=newName
        db.session.commit()
        return redirect(url_for('admin_tables'))
    return render_template('admin/testimonials-update.html',testimonial=testimonial,form=form)

@app.route('/admin/testimonials/delete/<id>',methods=['GET','POST'])
def admin_testimonial_delete(id):
    testimonial=Testimonials.query.get(id)
    db.session.delete(testimonial)
    db.session.commit()
    return redirect(url_for('admin_tables'))
 
      
@app.route('/admin/contact/',methods=['GET','POST'])
def admin_contact():
    form=ContactForm()
    if request.method=='POST':
        contact=Contact(
            contact_phone=form.contact_phone.data,
            contact_email=form.contact_email.data,
            contact_location=form.contact_location.data
        )
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for('admin_tables'))
    return render_template('admin/contact.html',form=form)
    

@app.route('/admin/contact-update/<id>',methods=['GET','POST'])
def admin_contact_update(id):
    contact=Contact.query.get(id)
    form=ContactForm()

    if request.method=='POST':
        
        contact.contact_phone=form.contact_phone.data
        contact.contact_email=form.contact_email.data
        contact.contact_location=form.contact_location.data
        db.session.commit()
        return redirect(url_for('admin_tables'))
    return render_template('admin/contact-update.html',contact=contact,form=form)

@app.route('/admin/contact/delete/<id>',methods=['GET','POST'])
def admin_contact_delete(id):
    contact=Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('admin_tables'))
 

@app.route('/admin/social-links/',methods=['GET','POST'])
def admin_social_link():
    form=SocialLinksForm()
    if request.method=='POST':
        link=SocialLinks(
            s_icon=form.s_icon.data,
            s_icon_url=form.s_icon_url.data
        )
        db.session.add(link)
        db.session.commit()
        return redirect(url_for('admin_tables'))
    return render_template('admin/social-links.html',form=form)
    
@app.route('/admin/social-links-update/<id>',methods=['GET','POST'])
def admin_social_link_update(id):
    link=SocialLinks.query.get(id)
    form=SocialLinksForm()
    if request.method=='POST': 
        link.s_icon=form.s_icon.data
        link.s_icon_url=form.s_icon_url.data   
        db.session.commit()
        return redirect(url_for('admin_tables'))
    return render_template('admin/social-link-update.html',link=link,form=form)

@app.route('/admin/social-link/delete/<id>',methods=['GET','POST'])
def admin_social_link_delete(id):
    link=SocialLinks.query.get(id)
    db.session.delete(link)
    db.session.commit()
    return redirect(url_for('admin_tables'))
 
@app.route('/admin/features/',methods=['GET','POST'])
def admin_feature():
    form=FeaturesForm()
    if request.method=='POST':
        features=Features(
            f_icon=form.f_icon.data,
            f_title=form.f_title.data,
            f_text=form.f_text.data
        )
        db.session.add(features)
        db.session.commit()
        return redirect(url_for('admin_tables'))
    return render_template('admin/features.html',form=form)
    
@app.route('/admin/features-update/<id>',methods=['GET','POST'])
def admin_feature_update(id):
    feature=Features.query.get(id)
    form=FeaturesForm()
    if request.method=='POST':      
        feature.f_icon=form.f_icon.data
        feature.f_title=form.f_title.data
        feature.f_text=form.f_text.data     
        db.session.commit()
        return redirect(url_for('admin_tables'))
    return render_template('admin/features-update.html',feature=feature,form=form)

@app.route('/admin/features/delete/<id>',methods=['GET','POST'])
def admin_feature_delete(id):
    feature=Features.query.get(id)
    db.session.delete(feature)
    db.session.commit()
    return redirect(url_for('admin_tables'))
 
    
 
