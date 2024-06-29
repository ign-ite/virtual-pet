from lastfmapi import GetGenre
import random
import pygame

lastfm = GetGenre()
artist, song = lastfm.last_fm_playing()
get_genre = lastfm.track_get_info(artist, song)
print(get_genre)


class SlimeSelect:
    def __init__(self, genre):
        self.path = 'Assets/'
        self.genre = genre
        self.genre = self.genre
        self.green_tags = ('folk', 'ambient', 'experimental', 'singer-songwriter', 'acoustic', 'chillout')
        self.blue_tags = ('electronic', 'indie', 'pop', 'ambient', 'electronica', 'house', 'techno')
        self.red_tags = ('rock', 'metal', 'punk', 'hardcore', 'thrash metal', 'progressive rock', 'heavy metal')
        self.all_tags = self.red_tags + self.green_tags + self.blue_tags
        self.current_slime = ''
        self.slimes = ['Blue_Slime', 'Green_Slime', 'Red_Slime']
        self.count = 0

    def select_slime(self):
        if self.genre not in self.all_tags:
            self.current_slime_index = random.randint(0, len(self.slimes) - 1)
            self.current_slime = self.slimes[self.current_slime_index]
            self.action = self.random_todo()
            self.count = self.frame_count()
            self.current_slime_dir = self.path + self.current_slime + self.action
            self.current_slime_images = []
            while len(self.current_slime_images) != self.count:
                for i in range(1, self.count + 1):
                    self.current_slime_image_temp = pygame.image.load(
                        self.current_slime_dir + '/' + f"{self.action}{i}.png").convert_alpha()
                    self.current_slime_image_temp = pygame.transform.scale(self.current_slime_image_temp, (150, 150))
                    self.current_slime_images.append(self.current_slime_image_temp)
            return self.current_slime_images
        else:
            if self.genre in self.red_tags:
                self.current_slime = self.slimes[2]
                self.action = '/Jump'
                self.count = 13
                self.current_slime_dir = self.path + self.current_slime + self.action
                self.current_slime_images = []
                while len(self.current_slime_images) != self.count:
                    for i in range(1, self.count + 1):
                        self.current_slime_image_temp = pygame.image.load(
                            self.current_slime_dir + '/' + f"{self.action}{i}.png").convert_alpha()
                        self.current_slime_image_temp = pygame.transform.scale(self.current_slime_image_temp,
                                                                               (150, 150))
                        self.current_slime_images.append(self.current_slime_image_temp)
                return self.current_slime_images
            elif self.genre in self.green_tags:
                self.current_slime = self.slimes[1]
                self.action = '/Walk'
                self.count = 8
                self.current_slime_dir = self.path + self.current_slime + self.action
                self.current_slime_images = []
                while len(self.current_slime_images) != self.count:
                    for i in range(1, self.count + 1):
                        self.current_slime_image_temp = pygame.image.load(
                            self.current_slime_dir + '/' + f"{self.action}{i}.png").convert_alpha()
                        self.current_slime_image_temp = pygame.transform.scale(self.current_slime_image_temp,
                                                                               (150, 150))
                        self.current_slime_images.append(self.current_slime_image_temp)
                return self.current_slime_images
            elif self.genre in self.blue_tags:
                self.current_slime = self.slimes[0]
                self.action = '/Run'
                self.count = 7
                self.current_slime_dir = self.path + self.current_slime + self.action
                self.current_slime_images = []
                while len(self.current_slime_images) != self.count:
                    for i in range(1, self.count + 1):
                        self.current_slime_image_temp = pygame.image.load(
                            self.current_slime_dir + '/' + f"{self.action}{i}.png").convert_alpha()
                        self.current_slime_image_temp = pygame.transform.scale(self.current_slime_image_temp,
                                                                               (150, 150))
                        self.current_slime_images.append(self.current_slime_image_temp)
                return self.current_slime_images

    def random_todo(self):
        self.to_do_list = ['/Run', '/Jump', '/Walk']
        self.to_do = random.choice(self.to_do_list)
        if self.to_do == '/Jump':
            self.count = 13
        elif self.to_do == '/Walk':
            self.count = 8
        else:
            self.count = 7
        return self.to_do

    def frame_count(self):
        if self.genre in self.red_tags:
            self.count = 13
            return self.count
        elif self.genre in self.green_tags:
            self.count = 8
            return self.count
        else:
            self.count = 7
            return self.count
