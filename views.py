from flask import Flask, url_for, render_template, request
import pymysql
import os

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello():
    return render_template('login.html')


@app.errorhandler(404)
def page_not_found(e):
    os.system('foxmail.py')
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    os.system('foxmail.py')
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
