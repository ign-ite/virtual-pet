import pygame
import random
from lastfmapi import GetGenre
import time
import win32gui
import win32api
import win32con

pygame.init()

BG_COLOR = (255, 255, 255)
info = pygame.display.Info()
(WIDTH, HEIGHT) = (info.current_w, info.current_h)

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
slime_path = 'Assets/'
slimes = ['Blue_Slime', 'Green_Slime', 'Red_Slime']
screen.fill(BG_COLOR)

all_slime_idle_images = []

for i in range(len(slimes)):
    slime = slime_path + slimes[i]
    slime_idle_path = slime + '/Idle'
    slime_idle_image = []
    while len(slime_idle_image) != 8:
        for i in range(1, 9):
            slime_idle_image_temp = pygame.image.load(slime_idle_path + '/' + f"Idle{i}.png").convert_alpha()
            slime_idle_image_temp = pygame.transform.scale(slime_idle_image_temp, (150, 150))
            slime_idle_image.append(slime_idle_image_temp)
    all_slime_idle_images.append(slime_idle_image)

blue_slime_idle_images = all_slime_idle_images[0]
green_slime_idle_images = all_slime_idle_images[1]
red_slime_idle_images = all_slime_idle_images[2]

frame_index = 0
frame_count = len(slime_idle_image)
clock = pygame.time.Clock()
animation_speed = 12

# Initialize slime position and movement
x_pos = random.randint(0, WIDTH - 150)
y_pos = random.randint(0, HEIGHT - 150)
x_speed = random.choice([-1, 1]) * random.uniform(1, 3)
y_speed = random.choice([-1, 1]) * random.uniform(1, 3)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    x_pos += x_speed
    y_pos += y_speed

    if x_pos <= 0 or x_pos >= WIDTH - 150:
        x_speed = -x_speed
    if y_pos <= 0 or y_pos >= HEIGHT - 150:
        y_speed = -y_speed

    screen.fill(BG_COLOR)

    hwnd = pygame.display.get_wm_info()["window"]
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(255, 255, 255), 0, win32con.LWA_COLORKEY)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

    frame_index = (frame_index + 1) % frame_count

    screen.blit(slime_idle_image[frame_index], (x_pos, y_pos))
    pygame.display.flip()

    clock.tick(animation_speed)

pygame.quit()
