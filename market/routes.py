from flask import render_template, redirect, url_for
from market import app, db
from market.models.Item import Item
from market.models.User import User
from market.forms.Register import Register


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = Item.query.all()

    return render_template('market.html', items=items)


@app.route('/login')
def login_page():
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = Register()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('market_page'))
    return render_template('register.html', form=form)
