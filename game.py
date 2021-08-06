import pygame
import config
from player import Player
from game_state import GameState
from tallgrass import TallGrass
import tallgrass
from pokegen import Pokegen
import pokegen
counter =0
wBattleCounter = 0
pointerx = 550
pointery = 580

class Game:


    def __init__(self, screen):

        self.screen = screen
        self.objects = []
        self.game_state = GameState.NONE
        self.map = []
        self.tallgrass = TallGrass()
        self.pokegen = Pokegen()

    def play_music(self):
            pygame.mixer.init()
            pygame.mixer.music.load('aud/route1.ogg')
            pygame.mixer.music.play(0, 0.0, 0)


    def set_up(self):
        player = Player(1, 1)
        self.player = player
        self.objects.append(player)
        print("do set up")
        self.game_state = GameState.RUNNING
        self.load_map("01")
        self.play_music()



    def update(self):

        self.screen.fill(config.BLACK)

        if tallgrass.wildEnc==True:
            self.handle_encounter()
            self.wild_encounter(self.screen)
        else:
            self.handle_events()
            self.render_map(self.screen)
            for object in self.objects:
                object.render(self.screen)



    def handle_events(self):
        pygame.key.set_repeat(1,100)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.game_state = GameState.ENDED
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = GameState.ENDED
                elif event.key == pygame.K_UP: # up
                    self.player.update_position_up()
                elif event.key == pygame.K_DOWN: # down
                    self.player.update_position_down()
                elif event.key == pygame.K_LEFT: # up
                    self.player.update_position_left()
                elif event.key == pygame.K_RIGHT: # up
                    self.player.update_position_right()

    def handle_encounter(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = GameState.ENDED
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = GameState.ENDED

    def load_map(self, file_name):
        with open('maps/' + file_name + ".txt") as map_file:
            for line in map_file:
                tiles = []
                for i in range(0, len(line), 2):
                    tiles.append(line[i])
                self.map.append(tiles)
            print(self.map)
            return tiles


    def render_map(self, screen):
        y_pos = 0
        for line in self.map:
            x_pos = 0
            for tile in line:
                image = map_tile_image[tile]
                maptiles = pygame.Rect(x_pos * config.SCALE, y_pos * config.SCALE, config.SCALE, config.SCALE)
                screen.blit(image, maptiles)

                x_pos = x_pos + 1

            y_pos = y_pos + 1

    def wild_encounter(self, screen):
        global counter
        global wBattleCounter
        global pointerx
        global pointery
        self.pokemon = pokegen.pokemon
        self.pokemonName = pokegen.pokemonName
        self.pokemonLvl = pokegen.pokemonLvl
        pkmX = 680
        pkmY = 160
        image = pygame.image.load('imgs/wildencounter.jpeg')
        image = pygame.transform.scale(image, (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        rect = pygame.Rect(0,0,config.SCREEN_WIDTH,config.SCREEN_HEIGHT)
        screen.blit(image, rect)
        self.pokemon = pygame.image.load('imgs/pkm/'+self.pokemon+'.png')
        self.pokemon = pygame.transform.scale(self.pokemon, (config.pokemonSCALE, config.pokemonSCALE))
        self.pkRect = pygame.Rect(pkmX, pkmY, config.SCALE, config.SCALE)
        screen.blit(self.pokemon, self.pkRect)
        self.font = pygame.font.Font('imgs/font.ttf', 62)
        self.encounterTxt = self.font.render(self.pokemonName, True, config.BLACK)
        screen.blit(self.encounterTxt, (90, 90))
        self.lvl = self.font.render(self.pokemonLvl, True, config.BLACK)
        screen.blit(self.lvl, (383, 93))

        for ev in pygame.event.get():
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RIGHT and pointerx == 550 and pointerx <= 730:
                    pointerx = pointerx + 180
                elif ev.key == pygame.K_LEFT and pointerx >= 550 and pointerx == 730:
                    pointerx = pointerx - 180
                elif ev.key == pygame.K_a:
                    if pointerx ==550 and counter ==2:
                        print('battle')
                        wBattleCounter = 1
                    elif pointerx == 730 and counter ==2 and wBattleCounter==0:
                        pygame.mixer.init()
                        pygame.mixer.music.load('aud/route1.ogg')
                        pygame.mixer.music.play(0, 0.0, 0)
                        tallgrass.wildEnc = False
                        counter = 0
                        wBattleCounter = 0
                    else:
                        counter += 1
                        if counter >2:
                            counter =2
                elif ev.key == pygame.K_s:
                    counter -=1
                    if counter <2:
                        counter = 2
                    wBattleCounter = 0

        if counter == 0:
            self.playertxt = self.font.render('A Wild '+self.pokemonName+' Appeared!', True, config.WHITE)
            screen.blit(self.playertxt, (68, 580))


        elif counter == 1:
            self.playermon = pygame.image.load('imgs/pkm/charmander.png')
            self.playermon = pygame.transform.scale(self.playermon, (config.pokemonSCALE, config.pokemonSCALE))
            screen.blit(self.playermon, (150, 380))
            self.playertxt = self.font.render('Go Charmander!', True, config.WHITE)
            screen.blit(self.playertxt, (68, 580))
            self.font = pygame.font.Font('imgs/font.ttf', 62)
            self.playermontxt = self.font.render('Charmander', True, config.BLACK)
            screen.blit(self.playermontxt, (600, 365))
            self.lvl = self.font.render('15', True, config.BLACK)
            screen.blit(self.lvl, (910, 365))

        elif counter == 2:
            #reloading playermon
            self.playermon = pygame.image.load('imgs/pkm/charmander.png')
            self.playermon = pygame.transform.scale(self.playermon, (config.pokemonSCALE, config.pokemonSCALE))
            screen.blit(self.playermon, (150, 380))
            self.playermontxt = self.font.render('Charmander', True, config.BLACK)
            screen.blit(self.playermontxt, (600, 365))
            self.lvl = self.font.render('15', True, config.BLACK)
            screen.blit(self.lvl, (910, 365))

            if wBattleCounter == 1:
                self.playertxt = self.font.render('What will', True, config.WHITE)
                screen.blit(self.playertxt, (68, 580))
                self.txt2ndline = self.font.render('Charmnder do?', True, config.WHITE)
                screen.blit(self.txt2ndline, (68, 650))
                self.fighttxt = self.font.render('Scratch', True, config.WHITE)
                screen.blit(self.fighttxt, (600, 580))
                self.runtxt = self.font.render('Ember', True, config.WHITE)
                screen.blit(self.runtxt, (780, 580))
                self.pointer = pygame.image.load('imgs/pointer.png')
                self.pointer = pygame.transform.scale(self.pointer, (50, config.SCALE))
                screen.blit(self.pointer, (pointerx, pointery))

            else:
                self.playertxt = self.font.render('What will', True, config.WHITE)
                screen.blit(self.playertxt, (68, 580))
                self.txt2ndline = self.font.render('Charmnder do?', True, config.WHITE)
                screen.blit(self.txt2ndline, (68, 650))
                self.fighttxt = self.font.render('Fight', True, config.WHITE)
                screen.blit(self.fighttxt, (600, 580))
                self.runtxt = self.font.render('Run', True, config.WHITE)
                screen.blit(self.runtxt, (780, 580))
                self.pointer = pygame.image.load('imgs/pointer.png')
                self.pointer = pygame.transform.scale(self.pointer, (50, config.SCALE))
                screen.blit(self.pointer, (pointerx, pointery))









        print(counter)















map_tile_image = {
    "G": pygame.transform.scale(pygame.image.load("maps/Grass.png"), (config.SCALE, config.SCALE)),
    "P": pygame.transform.scale(pygame.image.load("maps/PathTop.png"), (config.SCALE, config.SCALE)),
    "Q": pygame.transform.scale(pygame.image.load("maps/PathMid.png"), (config.SCALE, config.SCALE)),
    "X": pygame.transform.scale(pygame.image.load("maps/PathBottom.png"), (config.SCALE, config.SCALE)),
    "M": pygame.transform.scale(pygame.image.load("maps/PathMM.png"), (config.SCALE, config.SCALE)),
    "C": pygame.transform.scale(pygame.image.load("maps/PathTM.png"), (config.SCALE, config.SCALE)),
    "V": pygame.transform.scale(pygame.image.load("maps/PathBM.png"), (config.SCALE, config.SCALE)),
    "Z": pygame.transform.scale(pygame.image.load("maps/PathTopL.png"), (config.SCALE, config.SCALE)),
    "Y": pygame.transform.scale(pygame.image.load("maps/PathMidL.png"), (config.SCALE, config.SCALE)),
    "T": pygame.transform.scale(pygame.image.load("maps/TGrass.png"), (config.SCALE, config.SCALE)),


}