from flask import Flask, render_template, redirect, Blueprint, url_for
from views import my_view

app = Flask(__name__)
#app.config['SECRET KEY'] = 'This is a sentence'

app.register_blueprint(my_view)

@app.errorhandler(404)
def error_message(e):
    return render_template('error.html', e=e)



if __name__=='__main__':
    app.run(debug=True, port=8000)