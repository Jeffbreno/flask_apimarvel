import hashlib
import requests
from rich import print
from rich.console import Console
from rich.table import Table
import datetime

console = Console()

timestamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')
pub_key = '2fdf3882e0d438d46d210cd50a7229f5'
priv_key = '7043e5637186ff32aa617add10dc2ee3e302f02a'

def compute_md5_hash(my_string):
    '''
    Converte string em md5 hash.
    https://stackoverflow.com/a/13259879/802542
    '''
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()

def make_authorization():    
    ts = 1
    md5_hash = compute_md5_hash(f'{ts}{priv_key}{pub_key}')
    query_params = f'?ts={ts}&apikey={pub_key}&hash={md5_hash}'
    return query_params

def main():
    url = 'http://gateway.marvel.com/v1/public/characters?name=Agents%20of%202Atlas'
    url += make_authorization()
    with requests.Session() as session:
        response = session.get(url)
        print(response)
        characters = response.json()['data']['results']

        table = Table(title='Marvel characters')
        headers = (
            'id',
            'name',
            'description',
        )

        for header in headers:
            table.add_column(header)

        for character in characters:
            values = str(character['id']), str(character['name']), str(character['description'])
            table.add_row(*values)

        console.print(table)


if __name__ == '__main__':
    main()

# def getAll():

#     return True

# def getId(id):

#     return True

# def getNome(nome):

#     return True

