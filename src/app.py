from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from config import config 
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required

#Models
from models.ModelUser import ModelUser

#Entities
from models.entities.User import User

app=Flask(__name__)

csrf=CSRFProtect()
db=MySQL(app)
login_manager_app=LoginManager(app)

@login_manager_app.user_loader
def load_user(user_id):
    return ModelUser.get_user_by_id(db, user_id)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        # print(request.form['inputEmail'])
        # print(request.form['inputPassword']) 
        user=User(0,request.form['inputEmail'], request.form['inputPassword'])
        logged_user=ModelUser.login(db, user)
        if logged_user:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash('Password incorrecto')
                return redirect(url_for('login'))
            
        else:
            flash('Usuario no encontrado')
            return redirect(url_for('login'))
        
        return render_template('auth/login.html')
    return render_template('auth/login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/home')
@login_required
def home():
    return render_template('home.html')

@app.route('/protected')
@login_required
def protected():
    return "<h1>Hello, you are logged in!</h1>"

def status_401(error=None):
    return redirect(url_for('login'))

def status_404(error=None):
    return "<h1>404 Página no encontrada</h1>", 404
    



if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app) # Initialize CSRF protection
    app.register_error_handler(404, status_404)
    app.register_error_handler(401, status_401)
    app.run()