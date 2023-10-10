# AULA 09 - Templates em Flask

# 'render_template' vai renderizar o nosso template...
from flask import Flask, render_template

# Designando o nome da nossa pasta template...
app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('modelo.html')

if __name__ == '__main__':
    app.run(port='5000')

"""
Nesta mesma aula ele ensina como usar variáveis nos nossos templates, como eu já vi em Django,
resolvi pular esse parte...
"""