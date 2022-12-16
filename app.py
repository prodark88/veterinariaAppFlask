from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required
from config import config


#Model
from models.ModelUser import ModelUser

#entities
from models.entities.User import User
app = Flask(__name__)
db = MySQL(app)
login_manager_app=LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db,id)

#deespues y antes de una peticion
@app.before_request
def before_request():
    print("antes de la peticion")

@app.after_request 
def after_request(response):
    print("despues de la peticion")
    return response

#ruta raiz
@app.route('/')
def index():
    return redirect(url_for('login'))


#login o logout
@app.route('/login', methods=['GET', 'POST'] )
def login():
    if request.method=='POST':
        #print(request.form ['username'] )
        #print(request.form ['password'] )
        user=User(0,request.form ['username'],request.form ['password'])
        logget_user=ModelUser.login(db,user)
        if logget_user !=None:
            if logget_user.password:
                login_user(logget_user)
                return redirect (url_for('home'))
            else:
                flash("Contraseña incorrecta")
                return render_template('auth/login.html')
        else:
            flash("Usuario no encontrado")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/registro')
def registro():
    return render_template('registro.html')
'''
def pagina_no_encontrada(error):
    return render_template('404.html'), 404
    return redirect (url_for('index.html'))
'''




if __name__ =='__main__':
    app.config.from_object(config['development'])
    #app.register_error_handler(404,pagina_no_encontrada)
    app.run(debug=True, port=5000)
