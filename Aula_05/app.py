# AULA 05 - WEB Arquivos Estáticos.

from flask import Flask

# Definindo pasta arquivo estático...
app = Flask(__name__, static_folder = 'static')

# Não é necessário criar uma rota para acessar esse nosso arquivo estático.
if __name__ == '__main__':
    app.run()