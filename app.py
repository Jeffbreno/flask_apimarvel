from flask import Flask, render_template, request, redirect, session, flash


class Jogo:
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console


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
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login')
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST',])
def criar():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']
    jogo = Jogo(name, category, console)

    lista.append(jogo)

    return redirect('/')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if '123' == request.form['senha']:
        session['usuario'] = request.form['user']
        flash(session['usuario'] + ' logado com sucesso!')
        return redirect('/')
    else:
        flash('Usuário não logado com sucesso!')
        return redirect('/login')


@app.route('/logout')
def login():
    session['usuario'] = None
    flash('Logout efetuado com sucesso')
    return render_template('/')


app.run(debug=True, host='localhost', port=5225)
