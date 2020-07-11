from alien import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return alien.query.get(int(user_id))



class alien(db.Model,UserMixin):
    id=db.Column('id',db.Integer,primary_key=True)
    name=db.Column(db.String(20),nullable=False,unique=True)
    password=db.Column(db.String(20),nullable=False,unique=True)
    posts = db.relationship('Post', backref='author', lazy=True)
    def __repr__(self):
        return f'{self.name}'



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    alien_id = db.Column(db.Integer, db.ForeignKey('alien.id'), nullable=False)

    def __repr__(self):
        return f'{self.title}'