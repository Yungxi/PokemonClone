import pygame
import config
global x_postition
global y_position
from tallgrass import TallGrass
import mapcoords


speedX = 20
speedY=20
class Player:


    def __init__(self, x, y):
        print("player created")
        self.playerx = 0
        self.playery = 1
        self.image = pygame.image.load('imgs/player.png')
        self.image = pygame.transform.scale(self.image,(config.playerSCALE, config.playerSCALE))
        self.rect = pygame.Rect(self.playerx * config.playerSCALE, self.playery * config.playerSCALE, config.playerSCALE, config.playerSCALE)
        self.tallgrass = TallGrass()


    def update(self):
        print("player updated")


    playerStep = 0



    def update_position_up(self):
        time = 50 / 10000

        vel = time*config.SPEED

        # map edge
        if self.playery <0:
            return
        else:
            self.playery -= vel
            self.rect = pygame.Rect(self.playerx * config.playerSCALE, self.playery * config.playerSCALE, config.playerSCALE, config.playerSCALE)

        tallgrassC = self.rect.collidelist(mapcoords.checkCoords)
        if tallgrassC != -1:
            self.tallgrass.random_encounter()

        if self.playerStep == 0:
            self.image = pygame.image.load('imgs/Up1.png')
            self.image = pygame.transform.scale(self.image, (config.playerSCALE, config.playerSCALE))
            self.playerStep =1

        elif self.playerStep ==1:
            self.image = pygame.image.load('imgs/Up2.png')
            self.image = pygame.transform.scale(self.image, (config.playerSCALE, config.playerSCALE))
            self.playerStep =2

        elif self.playerStep == 2:
            self.image = pygame.image.load('imgs/Up3.png')
            self.image = pygame.transform.scale(self.image, (config.playerSCALE, config.playerSCALE))
            self.playerStep = 0



    def update_position_down(self):
        time = 50 / 10000

        vel = time * config.SPEED

        #map edge
        if self.playery-0.6 > 7.68:
            return
        else:
            self.playery += vel
            self.rect = pygame.Rect(self.playerx * config.playerSCALE, self.playery * config.playerSCALE, config.playerSCALE, config.playerSCALE)

        tallgrassC = self.rect.collidelist(mapcoords.checkCoords)
        if tallgrassC != -1:
            self.tallgrass.random_encounter()


        if self.playerStep == 0:
            self.image = pygame.image.load('imgs/Down1.png')
            self.image = pygame.transform.scale(self.image, (config.playerSCALE, config.playerSCALE))
            self.playerStep =1

        elif self.playerStep ==1:
            self.image = pygame.image.load('imgs/Down2.png')
            self.image = pygame.transform.scale(self.image, (config.playerSCALE, config.playerSCALE))
            self.playerStep =2

        elif self.playerStep == 2:
            self.image = pygame.image.load('imgs/Down3.png')
            self.image = pygame.transform.scale(self.image, (config.playerSCALE, config.playerSCALE))
            self.playerStep = 0



    def update_position_right(self):
        time = 50 / 10000
        vel = time * config.SPEED
        self.playerx += vel
        self.rect = pygame.Rect(self.playerx * config.playerSCALE, self.playery * config.playerSCALE, config.playerSCALE, config.playerSCALE)

        tallgrassC = self.rect.collidelist(mapcoords.checkCoords)
        if tallgrassC != -1:
            self.tallgrass.random_encounter()

        if self.playerStep == 0:
            self.image = pygame.image.load('imgs/Right1.png')
            self.image = pygame.transform.scale(self.image, (config.playerSCALE, config.playerSCALE))
            self.playerStep =1

        elif self.playerStep ==1:
            self.image = pygame.image.load('imgs/Right2.png')
            self.image = pygame.transform.scale(self.image, (config.playerSCALE, config.playerSCALE))
            self.playerStep =2

        elif self.playerStep == 2:
            self.image = pygame.image.load('imgs/Right3.png')
            self.image = pygame.transform.scale(self.image, (config.playerSCALE, config.playerSCALE))
            self.playerStep = 0



    def update_position_left(self):
        time = 50 / 10000
        vel = time * config.SPEED
        self.playerx -= vel
        self.rect = pygame.Rect(self.playerx * config.playerSCALE, self.playery * config.playerSCALE, config.playerSCALE, config.playerSCALE)

        tallgrassC = self.rect.collidelist(mapcoords.checkCoords)
        if tallgrassC != -1:
            self.tallgrass.random_encounter()


        if self.playerStep == 0:
            self.image = pygame.image.load('imgs/Left1.png')
            self.image = pygame.transform.scale(self.image, (config.playerSCALE, config.playerSCALE))
            self.playerStep =1

        elif self.playerStep ==1:
            self.image = pygame.image.load('imgs/Left2.png')
            self.image = pygame.transform.scale(self.image, (config.playerSCALE, config.playerSCALE))
            self.playerStep =2

        elif self.playerStep == 2:
            self.image = pygame.image.load('imgs/Left3.png')
            self.image = pygame.transform.scale(self.image, (config.playerSCALE, config.playerSCALE))
            self.playerStep = 0




    def render(self, screen):
        screen.blit(self.image, self.rect)


