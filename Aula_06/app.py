# AULA 06 - Métodos HTTP
"""
Principais métodos HTTP:
- GET (Quando queremos receber)
- POST (Quando queremos adicionar)
- PUT (Quando queremos editar)
- DELETE (Quando queremos deletar)
"""

from flask import Flask, request
from json import dumps

app = Flask(__name__, static_folder = 'static')

# Só teremos acesso a função 'add' se recebermos um método do tipo 'POST'
# @app.route('/add', methods=['POST'])
# def add():
#     return 'Usuário Adicionado!'

# Função apenas demonstrativa para entender melhor métodos 'GET' e 'POST'.
@app.route('/add', methods=['POST', 'GET'])
def add():
#   Se o método recebido pela requisição for 'POST' retorne um 'JSON' com as informações.
    if request.method == 'POST':
#       Retorna dicionário com a informação...        
        return dumps(request.form)
    else:
#       Mostrara 'GET' na tela...        
        return f'{request.method}'

if __name__ == '__main__':
    app.run()