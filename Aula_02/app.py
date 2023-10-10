# AULA 02 - Outra maneira de criar rotas e configurações.

from flask import Flask

app = Flask(__name__)

# Como vimos na 'Aula_01', podemos usar decoradores para indicar rotas...
@app.route('/')
def home():
    return 'Home Page!'

# Abaixo vemos outra maneira de fazer a mesma coisa que acima sem usar decoradores...
"""
def home():
    return 'Home Page!'
app.add_url_rule('/', 'home', home)
"""

def teste():
    return '<h1>Test Page!</h1>'
app.add_url_rule('/teste', 'teste', teste)

if __name__ == '__main__':
#   Usamos o 'debug = True' quando estamos em modo desenvolvimento...
#   Podemos também definir a porta, como visto abaixo...
    app.run(debug = True, port = 3000)