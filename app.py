from flask import Flask, render_template, request, redirect


class Jogo:
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console

jogo1 = Jogo('Mario', 'Campanha', 'Nitendo')
jogo2 = Jogo('League Of Legands', 'Estrategia', 'Computador')
lista = [jogo1, jogo2]


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('lista.html', title='Jogo', jogos=lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', title='Novo Jogo')


@app.route('/criar', methods=['POST',])
def criar():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']
    jogo = Jogo(name, category, console)

    lista.append(jogo)

    return redirect('/')

app.run(debug=True, host='localhost', port=5225)
