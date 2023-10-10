# AULA 01 - Instalando o flask e rodando primeiro código com o framework.

# Importando a biblioteca...
from flask import Flask

# Criando variável app, instancia de Flask...
app = Flask(__name__)

# Para definir rotas em Flask podemos utilizar de decoradores...
@app.route('/')
def index():
    return 'Index'

@app.route('/teste')
def teste():
    return 'Teste'

if __name__ == '__main__':
    app.run()