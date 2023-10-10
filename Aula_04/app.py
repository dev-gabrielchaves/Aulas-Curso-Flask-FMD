# AULA 04 - Construção de URL e redirect.

# Usamos o 'redirect' para redirecionar o para outra página.

# Usamos o url_for para passar o nome função na qual queremos redirecionar...
# Dessa maneira fica mais fácil, pois não temos que inserir toda a URL.
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/admin')
def admin():
    return 'Admin Page!'

@app.route('/guest/<guest>')
def guest(guest):
    return f'Welcome guest {guest}!'

# Criando rota user que irá redirecionar dependendo do parâmetro de entrada.
@app.route('/user/<name>')
def user(name):
    if name == 'admin':
#       Sem usar o 'url_for' para o redirecionamento...
        return redirect('/admin')
    else:
        return redirect(url_for('guest', guest = name))

if __name__ == '__main__':
    app.run(debug = True, port = 3000)