from flask import render_template, redirect,  url_for, Blueprint, request

my_view = Blueprint('my_view',__name__)

@my_view.route('/', methods=['POST', 'GET' ])
def home():
    return render_template('index.html')

@my_view.route('/home')
@my_view.route('/js')
@my_view.route('/javascript')
def home_redirect():
    return redirect(url_for('my_view.home'))

@my_view.route('/admin')
def admin():
    return render_template('admin.html')


@my_view.route('/intro')
def intro():
    return render_template('intro.html')

@my_view.route('/introduction')
def intro_redirect():
    return redirect(url_for('my_view.intro'))

@my_view.route('/events')
def events():
    return render_template('events.html')

@my_view.route('/extra/')
def extra():
    return render_template('extra.html')

