import random
wildEnc = False
import pygame

from pokegen import Pokegen
class TallGrass:

    def __init__(self):
        print('initialized')
        self.pokegen = Pokegen()

    def random_encounter(self):
        global wildEnc
        ran = random.randint(0,37)

        if ran <=1:
            print('encounter')
            self.pokegen.generate_pokemon()
            wildEnc = True
            pygame.mixer.stop()
            pygame.mixer.init()
            pygame.mixer.music.load('aud/wildEnc.ogg')
            pygame.mixer.music.play(0, 0.0, 0)



        else:
            print('none')

