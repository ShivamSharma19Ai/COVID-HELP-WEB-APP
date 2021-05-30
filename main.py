from os import close
from flask import Flask, render_template, request, session
import mysql.connector
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://chip:123@localhost/covaid'
db = SQLAlchemy(app)

class Register_db(db.Model):

    '''
    id,name registration no email password
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/covid19')
def covid19():
    return render_template('page.html')

@app.route('/posts')
def posts():
    return render_template('posts.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if (request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        user = Register_db.query.filter_by(username=username).first()
        if user:
            if user.password == password:
                return render_template('Index.html')
    else:
        return render_template('login.html')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if (request.method == 'POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        username= request.form.get('username')

        entry = Register_db(
            name=name,email=email,username=username, password=password)
        db.session.add(entry)
        db.session.commit()
    return render_template('register.html')

   

@app.route('/vaccinations')
def vaccinations():
    return render_template('vaccinations.html')


app.run(debug=True)
