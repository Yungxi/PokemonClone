import random
pokemon = ''
pokemonName = ''
pokemonLvl = 1

class Pokegen:

    def __init__(self):
        print('initialized')



    def generate_pokemon(self):
        global pokemon
        global pokemonName
        global pokemonLvl
        number = random.randint(0,1)
        numlvl = random.randint(12,15)
        pokemonLvl = str(numlvl)

        if number == 0:
            pokemon = 'nidoran-m'
            pokemonName = 'Nidoran'
        elif number == 1:
            pokemon = 'fletchling'
            pokemonName = 'Fletchling'


