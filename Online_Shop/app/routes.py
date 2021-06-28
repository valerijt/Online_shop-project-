from app import app
from flask import render_template, redirect, request
from app.forms import OrderForm
from app.models import Customer
from app.__init__ import db


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/support')
def support():
    return render_template('support.html')


@app.route('/validate', methods=['GET', 'POST'])
def validate():
    return render_template('validate.html')


@app.route('/order', methods=['GET', 'POST'])
def order():
    form = OrderForm()
    if form.validate_on_submit():
        return redirect('/validate')

    return render_template('order.html', form=form)
