import pygame
import random
import time
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


def update_position(x_pos, y_pos, x_speed, y_speed, slime_type):
    if slime_type == 'Blue_Slime':
        speed_multiplier = 1
    elif slime_type == 'Green_Slime':
        speed_multiplier = 1
    elif slime_type == 'Red_Slime':
        speed_multiplier = 1.5
    else:
        speed_multiplier = 1

    x_pos += x_speed * speed_multiplier
    y_pos += y_speed * speed_multiplier
    if x_pos <= 0 or x_pos >= WIDTH - 150:
        x_speed = -x_speed
    if y_pos <= 0 or y_pos >= HEIGHT - 150:
        y_speed = -y_speed
    return x_pos, y_pos, x_speed, y_speed


song_info = GetGenre()
artist, song = song_info.last_fm_playing()
genre = song_info.track_get_info(artist, song)
slime_selector = SlimeSelect(genre)
slime_images = slime_selector.get_images()
frame_index = 0
frame_count = slime_selector.get_frame_count()

clock = pygame.time.Clock()
animation_speed = 12

hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(255, 255, 255), 0, win32con.LWA_COLORKEY)
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

last_song_check = time.time()
check_interval = 5  # Check for song change every 5 seconds

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if time.time() - last_song_check >= check_interval:
        artist, song = song_info.last_fm_playing()
        new_genre = song_info.track_get_info(artist, song)
        if new_genre != genre:
            genre = new_genre
            slime_selector = SlimeSelect(genre)
            slime_images = slime_selector.get_images()
            frame_count = slime_selector.get_frame_count()
        last_song_check = time.time()

    x_pos, y_pos, x_speed, y_speed = update_position(x_pos, y_pos, x_speed, y_speed, slime_selector.current_slime)

    frame_index = (frame_index + 1) % frame_count

    screen.fill(BG_COLOR)
    screen.blit(slime_images[frame_index], (x_pos, y_pos))
    pygame.display.flip()

    clock.tick(animation_speed)

pygame.quit()
