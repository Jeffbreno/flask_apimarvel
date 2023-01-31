from flask import Flask, render_template, request, redirect, session, flash, url_for
# import conected_api_marvel


class Jogo:
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console


class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha


usuario = Usuario('Jefferson Lopes', 'jeffbreno', '123456')
usuario2 = Usuario('Daniel Bruno', 'daniellopes', '123456')

usuarios = {usuario.nickname: usuario,
            usuario2.nickname: usuario2}

jogo1 = Jogo('Mario', 'Campanha', 'Nitendo')
jogo2 = Jogo('League Of Legands', 'Estrategia', 'Computador')
lista = [jogo1, jogo2]


app = Flask(__name__)

app.secret_key = 'Flask_ApiMarvel'


@app.route('/')
def index():
    return render_template('lista.html', title='Jogo', jogos=lista)


@app.route('/novo')
def novo():
    if 'usuario' not in session or session['usuario'] == None:
        return redirect(url_for('login', pag=url_for('novo')))
    return render_template('novo.html', title='Novo Jogo')


@app.route('/criar', methods=['POST',])
def criar():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']
    jogo = Jogo(name, category, console)
    lista.append(jogo)

    return redirect(url_for('index'))


@app.route('/login')
def login():
    pag = request.args.get('pag')
    return render_template('login.html', pag=pag)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if request.form['user'] in usuarios:
        usuario = usuarios[request.form['user']]
        if request.form['password'] == usuario.senha:
            session['usuario'] = usuario.nickname
            flash(session['usuario'] + ' logado com sucesso!', 'success')
            next_page = request.form['pag']
            return redirect(next_page)
    else:
        flash('Usuário não logado com sucesso!', 'danger')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario'] = None
    flash('Logout efetuado com sucesso', 'success')
    return redirect(url_for('index'))


app.run(debug=True, host='localhost', port=5225)
