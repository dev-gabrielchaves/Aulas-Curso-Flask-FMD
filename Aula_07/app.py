# AULA 07 - Objetos de Requisição.

from flask import Flask, request
from json import dumps

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
#   Estarei imprimindo no meu terminal...
    print(request.method, request.args)
#   O request.args é basicamente uma string, para transformar em dicionário...
    dict_1 = dict(request.args)
#   Mostrando dicionário...
    return dumps(dict_1)

# Informações mostradas no terminal ao 'runnar' a aplicação...
# GET ImmutableMultiDict([])
# 127.0.0.1 - - [09/Oct/2023 15:13:54] "GET / HTTP/1.1" 200 -
# GET ImmutableMultiDict([('nome', 'Gabriel'), ('idade', '24')]) --> request.method request.args
# 127.0.0.1 - - [09/Oct/2023 15:14:39] "GET /?nome=Gabriel&idade=24 HTTP/1.1" 200 -

if __name__ == '__main__':
    app.run()