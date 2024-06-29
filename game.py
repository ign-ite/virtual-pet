import pygame
import random
from lastfmapi import GetGenre
from basic_functions import SlimeSelect
import win32gui
import win32api
import win32con


pygame.init()

BG_COLOR = (255, 255, 255)
info = pygame.display.Info()
(WIDTH, HEIGHT) = (info.current_w, info.current_h)

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
screen.fill(BG_COLOR)



x_pos = random.randint(0, WIDTH - 150)
y_pos = random.randint(0, HEIGHT - 150)
x_speed = random.choice([-1, 1]) * random.uniform(1, 3)
y_speed = random.choice([-1, 1]) * random.uniform(1, 3)


def green(x_pos, y_pos, x_speed, y_speed):
    x_pos = x_pos + x_speed
    y_pos = y_pos + y_speed
    if x_pos <= 0 or x_pos >= WIDTH - 150:
        x_speed = -x_speed
    if y_pos <= 0 or y_pos >= HEIGHT - 150:
        y_speed = -y_speed
    return x_pos, y_pos, x_speed, y_speed

run = True
while run:
    song_info = GetGenre()
    artist, song = song_info.last_fm_playing()
    genre = song_info.track_get_info(artist, song)
    slime = SlimeSelect(genre).select_slime()

    frame_index = 0
    frame_count = SlimeSelect(genre).frame_count()
    clock = pygame.time.Clock()
    animation_speed = 12

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if SlimeSelect(genre).current_slime == 'Blue_Slime':
        x_pos, y_pos, x_speed, y_speed = green(x_pos, y_pos, x_speed, y_speed)

    screen.fill(BG_COLOR)

    hwnd = pygame.display.get_wm_info()["window"]
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                           win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(255, 255, 255), 0, win32con.LWA_COLORKEY)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

    frame_index = (frame_index + 1) % frame_count

    screen.blit(slime[frame_index], (x_pos, y_pos))
    pygame.display.flip()

    clock.tick(animation_speed)

pygame.quit()
