from app import app
from flask import render_template, redirect, flash
from app.forms import OrderForm


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


@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/order', methods=['GET', 'POST'])
def order():
    form = OrderForm()
    if form.validate_on_submit():
        return redirect('/confirmation')
    return render_template('order.html', form=form)

