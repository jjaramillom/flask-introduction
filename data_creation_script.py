from market import db
from market.models.User import User
from market.models.Item import Item

users = [
    User(username='jac', password='123', email='jj@jj.com')
]

items = [
    Item(name='Iphone 10', description='bad phone', barcode='123456789123', price=800),
    Item(name='laptop', description='cool laptop', barcode='123456789124', price=1800)
]

for user in users:
    db.session.add(user)

for item in items:
    db.session.add(item)

db.session.commit()