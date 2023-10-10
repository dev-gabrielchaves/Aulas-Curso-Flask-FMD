# AULA 03 - Criando URL's dinâmicas.

from flask import Flask

app = Flask(__name__)

# Abaixo vemos um exemple de url dinâmica...
# Podemos setar mais de uma rota para a mesma função... 
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = ''): # 'Setando' name como '' by default.  
    return f'<h1>Hello {name}!</h1>'

if __name__ == '__main__':
    app.run(debug = True, port = 3000)