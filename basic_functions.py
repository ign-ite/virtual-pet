import random
import pygame
from lastfmapi import GetGenre

class SlimeSelect:
    def __init__(self, genre):
        self.path = 'Assets/'
        self.genre = genre
        self.green_tags = {'folk', 'ambient', 'experimental', 'singer-songwriter', 'acoustic', 'chillout'}
        self.blue_tags = {'electronic', 'indie', 'pop', 'electronica', 'house', 'techno'}
        self.red_tags = {'rock', 'metal', 'punk', 'hardcore', 'thrash metal', 'progressive rock', 'heavy metal'}
        self.all_tags = self.red_tags | self.green_tags | self.blue_tags
        self.slimes = {
            'Blue_Slime': (self.blue_tags, '/Run', 7),
            'Green_Slime': (self.green_tags, '/Walk', 8),
            'Red_Slime': (self.red_tags, '/Jump', 13)
        }
        self.current_slime = 'Blue_Slime'
        self.current_action = '/Run'
        self.frame_count = 7

        self.select_slime()

    def select_slime(self):
        if self.genre not in self.all_tags:
            self.current_slime = random.choice(list(self.slimes.keys()))
            self.current_action, self.frame_count = self.random_todo()
        else:
            for slime, (tags, action, count) in self.slimes.items():
                if self.genre in tags:
                    self.current_slime = slime
                    self.current_action = action
                    self.frame_count = count
                    break

        self.current_slime_images = self.load_images()

    def load_images(self):
        images = []
        slime_dir = f"{self.path}{self.current_slime}{self.current_action}"
        for i in range(1, self.frame_count + 1):
            image_path = f"{slime_dir}/{self.current_action}{i}.png"
            image = pygame.image.load(image_path).convert_alpha()
            image = pygame.transform.scale(image, (150, 150))
            images.append(image)
        return images

    def random_todo(self):
        to_do_list = [
            ('/Run', 7),
            ('/Jump', 13),
            ('/Walk', 8)
        ]
        return random.choice(to_do_list)

    def get_images(self):
        return self.current_slime_images

    def get_frame_count(self):
        return self.frame_count
