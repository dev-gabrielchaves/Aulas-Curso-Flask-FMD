# AULA 10 - Enviando dados para template.

from flask import Flask, request, render_template

# 'Linkando' folder template...
app = Flask(__name__, template_folder='templates')

@app.route('/')
def notas():
    return render_template('notas.html')

@app.route('/calculo', methods=['POST'])
def calculo():
#   Nossa variável total irá receber todos os valores do nosso formulário...
#   ...depois irá transformar todos esse valores em inteiros...
#   ...e finalmente os somara usando a função 'sum'...    
    total = sum([int(v) for v in request.form.to_dict().values()])
#   Retornando nosso template e passando para o mesmo a variável total que recebe total...
    return render_template('calculo.html', total=total)

if __name__ == '__main__':
    app.run(port="5000")