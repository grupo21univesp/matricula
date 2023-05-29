from flask import Flask, render_template, request, url_for, flash, redirect
import os, datetime
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import abort

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))

app = Flask('__name__')
app.config['SECRET_KEY'] = 'your secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
db = SQLAlchemy(app)

class Matricula(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    name = db.Column(db.String(80), nullable=False)
    born = db.Column(db.String(10), nullable=False)
    grad = db.Column(db.String(15), nullable=False)
    sch = db.Column(db.String(20), nullable=False)
    addr = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    uf = db.Column(db.String(2), nullable=False)
    resp = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    tel = db.Column(db.String(14), nullable=False)
    obs = db.Column(db.String(200), nullable=False)

@app.route('/')
def index():
    exibir = Matricula.query.all()
    return render_template('index.html', exibir=exibir)

def get_post(post_id):
    exibe = Matricula.query.filter_by(id=post_id).first()
    if exibe is None:
        abort(404)
    return exibe

@app.route('/<int:post_id>')
def post(post_id):
    qq = get_post(post_id)
    return render_template('post.html', post=qq)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        born = request.form['born']
        grad = request.form['grad']
        sch = request.form['sch']
        addr = request.form['addr']
        city = request.form['city']
        uf = request.form['uf']
        resp = request.form['resp']
        email = request.form['email']
        tel = request.form['tel']
        if not name:
            flash('O nome é obrigatório')
        else:
            post = Matricula(name=name, born=born, grad=grad, sch=sch, addr=addr, city=city, uf=uf, resp=resp, email=email, tel=tel)
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('protocolo'))

    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        name = request.form['name']
        born = request.form['born']
        grad = request.form['grad']
        sch = request.form['sch']
        addr = request.form['addr']
        city = request.form['city']
        uf = request.form['uf']
        resp = request.form['resp']
        email = request.form['email']
        tel = request.form['tel']
        obs = request.form['obs']

        if not name:
            flash('Nome é obrigatório!')
        else:
            post.name = name
            post.born = born
            post.grad = grad
            post.sch = sch
            post.addr = addr
            post.city = city
            post.uf = uf
            post.resp = resp
            post.email = email
            post.tel = tel
            post.obs = obs
            db.session.commit()
            return redirect(url_for('lista'))

    return render_template('edit.html', post=post)

@app.route('/lista')
def lista():
    exibir = Matricula.query.all()
    return render_template('lista.html', exibir=exibir)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    db.session.delete(post)
    db.session.commit()
    flash('"{}" foi apagado com sucesso!'. format(post.name))
    return redirect(url_for('index'))

@app.route('/protocolo', methods=('GET', 'POST'))
def protocolo():
    name = request.args.get('name')
    return render_template('protocolo.html', name=name)

@app.route('/consulta', methods=('GET', 'POST'))
def consulta():
    return render_template('consulta.html')

@app.route('/resultado', methods=('GET', 'POST'))
def resultado():
    name = request.args.get('name')
    if not name:
        return redirect('/consulta')
    id = request.args.get('id')
    if not id:
        return redirect('/consulta')
    post = get_post(id)

    return render_template('resultado.html', post=post, name=name, id=id)