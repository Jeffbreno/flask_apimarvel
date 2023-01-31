
import hashlib
import requests
import datetime

from pprint import pprint as pp

timestamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')
pub_key = '2fdf3882e0d438d46d210cd50a7229f5'
priv_key = '7043e5637186ff32aa617add10dc2ee3e302f02a'


def getAll():

    return True

def getId(id):

    return True

def getNome(nome):

    return True

def hash_params():
    """ Marvel API requires server side API calls to include
    md5 hash of timestamp + public key + private key """

    hash_md5 = hashlib.md5()
    hash_md5.update(f'{timestamp}{priv_key}{pub_key}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()

    return hashed_params


params = {'ts': timestamp, 'apikey': pub_key, 'hash': hash_params()}
res = requests.get('https://gateway.marvel.com:443/v1/public/characters',
                   params=params)

results = res.json()
# pp(results)
