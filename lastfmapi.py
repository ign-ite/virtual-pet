from __future__ import print_function
import os

import requests
from requests.exceptions import HTTPError, ConnectionError
from retry import retry
import yaml


class GetGenre:
    def __init__(self):
        self.lastfm_config = yaml.safe_load(
            open(os.path.expanduser('config/last-fm.yml')))
        self.lastfm_url_base = 'https://ws.audioscrobbler.com/2.0/'
        self.lastfm_user = self.lastfm_config['user']
        self.lastfm_key = self.lastfm_config['key']

    def update(self):
        artist, song = self.last_fm_playing()
        info = self.track_get_info(artist, song)
        print("Song info: {}".format(info))
        top_tags = self.get_top_tags()
        print(top_tags)

    @retry((HTTPError, ConnectionError), delay=1, backoff=2, tries=4)
    def last_fm_playing(self):
        params = {
            'method': 'user.getrecenttracks',
            'user': self.lastfm_user,
            'api_key': self.lastfm_key,
            'format': 'json',
            'limit': 1
        }
        try:
            req = requests.get(self.lastfm_url_base, params=params)
            req.raise_for_status()
            lfm_data = req.json()['recenttracks']
            if 'track' in lfm_data and lfm_data['track']:
                track = lfm_data['track'][0]
                if '@attr' in track and 'nowplaying' in track['@attr'] and track['@attr']['nowplaying'] == 'true':
                    artist = track['artist']['#text']
                    song = track['name']
                    return artist, song
            return 'None'
        except (KeyError, HTTPError, ConnectionError) as e:
            print(f"Error fetching Last.fm data: {e}")
            return 'None'

    @retry((HTTPError, ConnectionError), delay=1, backoff=2, tries=4)
    def track_get_info(self, artist, track_name):
        params = {
            'method': 'track.getinfo',
            'artist': artist,
            'track': track_name,
            'api_key': self.lastfm_key,
            'format': 'json'
        }
        try:
            req = requests.get(self.lastfm_url_base, params=params)
            req.raise_for_status()
            track_info = req.json().get('track')
            if track_info:
                top_tags = track_info['toptags']
                tag = top_tags['tag']
                genre = tag[0]['name']
                return genre
            return 'None'
        except (KeyError, HTTPError, ConnectionError) as e:
            print(f"Error fetching track info from Last.fm: {e}")
            return 'None'

    @retry((HTTPError, ConnectionError), delay=1, backoff=2, tries=4)
    def get_top_tags(self):
        params = {
            'method': 'tag.getTopTags',
            'api_key': self.lastfm_key,
            'format': 'json'
        }
        try:
            response = requests.get(self.lastfm_url_base, params=params)
            data = response.json()
            if 'toptags' in data and 'tag' in data['toptags']:
                return [tag['name'] for tag in data['toptags']['tag']]
            return []
        except:
            return 'None'

genre = GetGenre()
lastfm, song = genre.last_fm_playing()
print(lastfm)
print(song)
