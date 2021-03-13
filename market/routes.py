from flask import render_template, redirect, url_for, flash
from market import app, db
from market.models.Item import Item
from market.models.User import User
from market.forms.Register import Register
from market.forms.Login import Login


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = Item.query.all()

    return render_template('market.html', items=items)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = Login()

    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = Register()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}:
        for err in form.errors.values():
            flash(f'Error creating User. {err}', category='danger')
    return render_template('register.html', form=form)
