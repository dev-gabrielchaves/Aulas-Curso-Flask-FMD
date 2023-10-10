# AULA 11 - Cookies

from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setcookie')
def setcookie():
    return ''

@app.route('/getcookie')
def getcookie():
    return ''

if __name__ == '__main__':
    app.run()

# Vou adiantar esta aula por enquanto...