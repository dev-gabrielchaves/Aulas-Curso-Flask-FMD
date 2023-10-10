# AULA 12 - Session (REVISAR)

from flask import Flask, session, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates')
# Passando chave simples para fins ilustrativos...
app.secret_key = '12345'

# Definindo a rota como a página inicial...
@app.route('/')
def index():
#   Criando uma variável username e definindo ela como uma string vazia...
    username = ''
#   Caso o username estiver dentro da nossa session faça... Que no primeira caso não vai estar...
    if 'username' in session:
        username = session['username']
#   Retornando a nossa página index.html
    return render_template('index.html', username=username)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST' and request.form['username'] != '':
        session['username'] = request.form['username']
#       Redirecionando para a nossa função index... 
        return redirect(url_for('index'))
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()