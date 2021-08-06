import pickle
import os
os.system("clear")

playerPokemon = ['Charmander']

pickle.dump(playerPokemon,open('playerPokemon.dat','wb'))
print(playerPokemon)