from flask import Flask, render_template, request
import logging
import socket

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    if request.method == 'GET':  
        return render_template('index.html', hostname=hostname, ip_address=ip_address)
    else:
        selecao = request.form.get('selectTemp')
        valor = request.form.get('valorRef')

        try:
            valor = float(valor)
        except ValueError:
            return render_template('index.html', conteudo={'unidade': 'inválido', 'valor': 'Entrada inválida'}, hostname=hostname, ip_address=ip_address)

        if selecao == '1':
            resultado = valor / 1000
            unidade = "quilômetros"
        elif selecao == '2':
            resultado = valor * 1000
            unidade = "metros"
        elif selecao == '3':
            resultado = valor / 1609.34
            unidade = "milhas"
        elif selecao == '4':
            resultado = valor * 1609.34
            unidade = "metros"
        elif selecao == '5':
            resultado = valor * 3.28084
            unidade = "pés"
        elif selecao == '6':
            resultado = valor / 3.28084
            unidade = "metros"
        else:
            resultado = "Inválido"
            unidade = ""

        return render_template('index.html', conteudo={'unidade': unidade, 'valor': resultado}, hostname=hostname, ip_address=ip_address)

if __name__ == '__main__':
    app.run()
else:
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
