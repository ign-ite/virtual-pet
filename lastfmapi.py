from __future__ import print_function
import os
import time

import requests
from requests.exceptions import HTTPError, ConnectionError
from retry import retry
import yaml


class NPSlack:
    def __init__(self):
        self.lastfm_config = yaml.safe_load(
            open(os.path.expanduser('config/last-fm.yml')))
        self.lastfm_url_base = 'https://ws.audioscrobbler.com/2.0/'
        self.lastfm_user = self.lastfm_config['user']
        self.lastfm_key = self.lastfm_config['key']

        self.slack_config = yaml.safe_load(
            open(os.path.expanduser('config/slack.yml')))
        self.slack_url_base = 'https://slack.com/api/'
        self.slack_key = self.slack_config['key']

    def update(self):
        print('Getting data from Last.fm...', end='')
        lfm = self.last_fm_playing()
        if lfm is not None:
            print("Now playing: {}".format(lfm), ':headphones:')
        else:
            print('Nothing playing;', end='')

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
                    result = "{} - {}".format(artist, song)
                    return result
            return None
        except (KeyError, HTTPError, ConnectionError) as e:
            print(f"Error fetching Last.fm data: {e}")
            return None

    @retry((HTTPError, ConnectionError), delay=1, backoff=2, tries=4)
    def slack_status(self, text, emoji):
        profile = {
            'status_text': text,
            'status_emoji': emoji
        }
        params = {
            'token': self.slack_key,
            'profile': profile
        }
        try:
            req = requests.post(f"{self.slack_url_base}users.profile.set", json=params)
            req.raise_for_status()
        except (HTTPError, ConnectionError) as e:
            print(f"Error updating Slack status: {e}")


def main():
    np_slack = NPSlack()
    while True:
        try:
            np_slack.update()
            time.sleep(15)
        except (KeyboardInterrupt, SystemExit):
            exit()


if __name__ == "__main__":
    main()
