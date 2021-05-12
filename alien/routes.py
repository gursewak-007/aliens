from flask import render_template,redirect,request,url_for,flash
from alien import app, db, bcrypt
from alien.forms import regform, logform,postform
from alien.models import alien,Post
from flask_login import login_user, current_user, logout_user, login_required




@app.route("/" , methods=['GET','POST'])
def main():
    if current_user.is_authenticated:
        return redirect(url_for('post'))
    else:
        try:all=Post.query.all()
        except:all=0
    return render_template("index.html" ,posts=all)
@app.route("/login" , methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('post'))
    form=logform()
    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.name.data
            password =form.password.data
            try:
                u=alien.query.filter_by(name=name).first()
                if u and bcrypt.check_password_hash(u.password,password):
                    login_user(u,remember=form.remember.data)
                    return redirect(url_for('post'))
                else:
                    raise(PermissionError)
            except:flash('Login Unsuccessful. Please check name and password', 'danger')
                 
            
    return render_template("login.html" ,form=form)
@app.route("/reg" , methods=['GET','POST'])
def reg():
    form=regform()
    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.name.data
            hpassword =bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            q=alien(name=name,password=hpassword)
            db.session.add(q)
            try :
                db.session.commit()
                flash(f'Registeration for {form.name.data}','success')
                return redirect('/')
            except :
                flash(f'Registeration for {form.name.data} check name !','failed')
                return redirect('/reg')
    else:
        return render_template("reg.html",form=form)


@app.route("/post" , methods=['GET','POST'])
@login_required
def post():
    form=postform()
    if request.method=='POST':
        alien = current_user.id
        title=form.title.data
        content = form.content.data
        q=Post(title=title,content=content,alien_id=alien)
        db.session.add(q)
        db.session.commit()
        return redirect('/post')
    if request.method=='GET':
        try:all=Post.query.all()
        except:all=0
        return render_template('post.html',form=form,posts=all)
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main'))