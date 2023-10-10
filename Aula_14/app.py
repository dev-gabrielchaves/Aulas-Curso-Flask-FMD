# AULA 14 - CRUD em Flask com SQLAlchemy (REVISAR)

# Para fazer a utilização da biblioteca SQLAlchemy, fazer a sua instalação...
# ... digitar no prompt: 'pip install flask-sqlalchemy'.

from flask import Flask, render_template, request, url_for, redirect
# Importando a biblioteca SQLAlchemy...
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')

# Setando configurações do DB...
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db' # Apontando para o DB que vamos usar...

# Criando o DB...
db = SQLAlchemy(app)
app.app_context().push() # --> Revisar tópico <--

# Criando a tabela 'Usuario'...
class User(db.Model):
#   Dentro da classe 'Usuario' eu vou definir as minhas colunas...
#   Na coluna id, que sera a nossa PK, adicionando autoincremento e o tipo inteiro...
    id = db.Column('user_id', db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(100))
    age = db.Column(db.Integer)

#   Criando método '__init__' para instâncias...
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

@app.route('/')
def index():
#   Passando todos os dados da nossa tabela para a variável 'users'...
    users = User.query.all()
#   Passando a variável para o nosso arquivo 'index.html'...
    return render_template('index.html', users = users)

@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
#       Criando objeto usuário instância da nossa classe 'User' e passando os argumentos que são...
#       ...os valores que recebemos do formulário em 'add.html'. 
        user = User(request.form['first_name'], request.form['last_name'], request.form['age'])
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('add.html')

# Redirecionamento feito na linha '40' no 'index.html'...    
@app.route('/delete/<int:id>')
def delete(id):
#   Queremos apenas pegar o usuário pelo o 'id'...
    user = User.query.get(id)
#   Da mesma forma que fizemos no add, chamamos o DB e para fazer o comando 'commitamos'...
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))

"""O 'EDIT' é uma mistura do 'ADD' com o 'DELETE',
pois retornaremos a mesma página de adicionar, porém com os valores 'antigos',
e para enviar esse usuário para podermos altera-lo devemos pegar o 'id' e recolher
ele no nosso banco de dados."""
@app.route('/edit/<int:id>', methods=['POST', 'GET'])
def edit(id):
    user = User.query.get(id)
    if request.method == 'POST':
        user.first_name = request.form['first_name']
        user.last_name = request.form['last_name']
        user.age = request.form['age']
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('edit.html', user=user)
if __name__ == '__main__':
#   Criando a nossa estrutura do banco de dados...
    db.create_all()
    app.run(debug=True)