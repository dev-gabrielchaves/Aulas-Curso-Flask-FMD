# AULA 08- Redirecionamento e erros

from flask import Flask, request, abort, redirect, url_for

app = Flask(__name__, static_folder="static")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['name'] == 'admin' and request.form['password'] == 'admin':
            return redirect(url_for('success'))
        else:
#           Erro -- Não Autorizado...
            abort(401)
    else:
#       Erro -- Forbidden
        abort(403)

@app.route('/success')
def success():
    return 'Success!!'

if __name__ == '__main__':
    app.run(port="5000")