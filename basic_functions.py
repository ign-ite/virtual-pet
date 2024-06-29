from lastfmapi import GetGenre
import random


lastfm = GetGenre()
artist, song = lastfm.last_fm_playing()
get_genre = lastfm.track_get_info(artist, song)
print(get_genre)



class SlimeSelect:
    def __init__(self, genre, green_tags, blue_tags, red_tags, all_tags):
        self.path = 'Assets/'
        self.genre = genre
        self.green_tags = ('Folk', 'Ambient', 'Experimental', 'Singer-songwriter', 'Acoustic', 'Chillout')
        self.blue_tags = ('Electronic', 'Indie', 'Pop', 'Ambient', 'Electronica', 'House', 'Techno')
        self.red_tags = ('Rock', 'Metal', 'Punk', 'Hardcore', 'Thrash metal', 'Progressive rock', 'Heavy metal')
        self.all_tags = self.red_tags + self.green_tags + self.blue_tags
        self.current_slime = ''
        self.slimes = ['Blue_Slime', 'Green_Slime', 'Red_Slime']

    def select_slime(self):
        if self.genre not in self.all_tags:
            self.current_slime_index = random.randint(0, len(self.slimes)-1)
            self.current_slime = self.slimes[self.current_slime_index]
            self.current_slime_dir = self.path+self.current_slime

        else:

    def random_todo(self):
        self.to_do_list = ['/Idle', '/Run', '/Jump', '/Walk']
        self.to_do = random.choice(self.to_do_list)
        return self.to_do