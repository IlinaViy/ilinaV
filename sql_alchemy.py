from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdb1.db' 
db = SQLAlchemy(app) 

from datetime import datetime

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    login = db.Column(db.String(80), unique=True, nullable=True)
    password = db.Column(db.Integer, unique=True, nullable=True)
    address = db.Column(db.String(80), nullable=True)
    mail = db.Column(db.String(80), unique=True, nullable=True)
    age = db.Column(db.String(80), nullable=True)
    date_reg = db.Column(db.DateTime, nullable=True)
    
    
    def __repr__(self):
        return f'{self.id} {self.name}'


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    about = db.Column(db.String(80), nullable=True)
    price = db.Column(db.Integer,nullable=False)
    category = db.Column(db.String(80), nullable=True)

    def __repr__(self):
        return f'{self.id} {self.name}'


class Basket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'),
        nullable=False)    
    kol_vo = db.Column(db.Integer, nullable=False)
      
    
    prod = db.relationship('Product',
        backref=db.backref('basket', lazy=False))
     

#db.create_all()

acc = Account(name="Mike", age = 15, date_reg=datetime.now())
#prod = Product(name = "Juice", price = 3)
#bas = Basket(kol_vo = 5, prod = prod)
db.session.add(acc)
#db.session.add(bas)
db.session.commit()