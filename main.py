from marvel import Marvel
import requests
from rich import print
from rich.console import Console
from rich.table import Table

console = Console()

PUBLIC_KEY = '2fdf3882e0d438d46d210cd50a7229f5'
PRIVATE_KEY = '7043e5637186ff32aa617add10dc2ee3e302f02a'

marvel = Marvel(PUBLIC_KEY=PUBLIC_KEY,
                PRIVATE_KEY=PRIVATE_KEY)

characters = marvel.characters


def main():

    personagens = characters.all(name="Black Panther")["data"]["results"]

    table = Table(title='Marvel characters')
    headers = (
        'id',
        'name',
        'description',
        'imagem'
    )

    for header in headers:
        table.add_column(header)

    for personagem in personagens:
        values = str(personagem['id']), str(
            personagem['name']), str(personagem['description'], str(personagem["thumbnail"]["path"]+"."+personagem["thumbnail"]["extension"]))
        table.add_row(*values)

    console.print(table)

if __name__ == '__main__':
    main()

# from marvel import Marvel

# PUBLIC_KEY = '2fdf3882e0d438d46d210cd50a7229f5'
# PRIVATE_KEY = '7043e5637186ff32aa617add10dc2ee3e302f02a'

# marvel = Marvel(PUBLIC_KEY=PUBLIC_KEY, 
# 	PRIVATE_KEY=PRIVATE_KEY)

# characters = marvel.characters

# my_char = characters.all(name="Black Panther")["data"]["results"]

# for char in my_char:
# 	print(char["id"], " | ", char["name"], " | ", char["thumbnail"]["path"],".",char["thumbnail"]["extension"])
# 	# for comic in char["comics"]["items"]:
# 	#     print(comic["name"])
# 	print("---------------------")
