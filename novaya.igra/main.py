import pygame as pg
import sys

W = 400
H = 300

sc = pg.display.set_mode((W, H))
sc.fill((100, 150, 200))

dog_surf = pg.image.load('dog.bmp')
dog_rect = dog_surf.get_rect(
    bottomright=(W, H))
sc.blit(dog_surf, dog_rect)

pg.display.update()

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()

    pg.time.delay(20)