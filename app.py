from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.before_request
def before_request():
    print("antes de la peticion")

@app.after_request 
def after_request(response):
    print("despues de la peticion")
    return response

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/')
def registro():
    return render_template('registro.html')

def pagina_no_encontrada(error):
    return render_template('404.html'), 404
    return redirect (url_for('index.html'))


if __name__ =='__main__':
    app.register_error_handler(404,pagina_no_encontrada)
    app.run(Debug=True, port=5000)
