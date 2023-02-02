from flask import Flask, render_template, request, redirect, session, flash, url_for
from marvel import Marvel
import math 
# import requests

PUBLIC_KEY = '2fdf3882e0d438d46d210cd50a7229f5'
PRIVATE_KEY = '7043e5637186ff32aa617add10dc2ee3e302f02a'

marvel = Marvel(PUBLIC_KEY=PUBLIC_KEY,
                PRIVATE_KEY=PRIVATE_KEY)

characters = marvel.characters

app = Flask(__name__)

def listPag():
    i = 1
    total = characters.all()["data"]["total"]
    ultima_pag = math.ceil(total / 30)
    paginas = []
    x = range(ultima_pag)

    for i in x:
        if(i > 0):
            paginas.append(i)

    return paginas

def pag(pagina):
    
    if(pagina == 1):
        pagina = 0

    offset = pagina * 30

    return offset

@app.route('/')
def index():

    characters = marvel.characters
    pagina = pag(int(request.args.get('pag')))

    personagens = characters.all(offset=pagina, limit=30)["data"]["results"]
    return render_template('marvel.html', title='Herois Marvel', personagens=personagens, paginas=listPag())

@app.route('/salvar')
def salvar():

    return True

app.run(debug=True, host='localhost', port=5225)