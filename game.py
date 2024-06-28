import pygame
from lastfmapi import GetGenre
import time


pygame.init()

BG_COLOR = (255, 255, 255)
(WIDTH, HEIGHT) = (150, 150)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
slime_path = 'Assets/'
slimes = ['Blue_Slime', 'Green_Slime', 'Red_Slime']
screen.fill(BG_COLOR)
value, count = 0, 0

run = True
while run:
    clock = pygame.time.Clock()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(BG_COLOR)

    slime = slime_path+slimes[0]
    slime_idle_path = slime+'/Idle'
    slime_idle_image = []
    while len(slime_idle_image) != 8:
        for i in range(1, 9):
            slime_idle_image_temp = pygame.image.load(slime_idle_path+'/'+f"Idle{i}.png")
            slime_idle_image.append(slime_idle_image_temp)

    while True:
        for i in slime_idle_image:
            clock.tick(12)
            screen.blit(i, (0, 0))
            pygame.display.flip()
