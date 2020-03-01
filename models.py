#encoding:utf-8

from exts import db

class User(db.Model):
    __tablename__ = 'user_info'
    nickname = db.Column(db.String(50),primary_key=True,autoincrement=False)
    password = db.Column(db.String(100),nullable=False)
    pw_secure_question = db.Column(db.String(50),nullable=False)
    pw_secure_answer = db.Column(db.String(100),nullable=False)