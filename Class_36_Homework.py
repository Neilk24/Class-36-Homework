import pygame
import random

pygame.init()

width, height = 400,400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sprite color changer thing person code thingamabob')

black = (0,0,0)
white = (255,255,255)

class ColorChangingSprite(pygame.sprite.Sprite):
    def __init__(self, x,y,width,height,color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x,y))

    def change_color(self):
        self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.image.fill(self.color)

sp1 = ColorChangingSprite(200, 250, 100, 100,(0, 0, 255))
sp2 = ColorChangingSprite(500, 250, 100, 100,(255, 0, 0))

all_sprites = pygame.sprite.Group(sp1, sp2)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            sp1.change_color()
            sp2.change_color()
    screen.fill('white')
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()