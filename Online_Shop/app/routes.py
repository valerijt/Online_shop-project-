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
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']

        customer = Customer(name=name, email=email, phone=phone, address=address)

        try:
            db.session.add(customer)
            db.session.commit()
            return redirect('/validate')
        except:
            return redirect('/index')
    else:
        return render_template('/order')