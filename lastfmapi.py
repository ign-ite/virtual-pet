import pylast

LASTFM_API_KEY = 'your_lastfm_api_key'
LASTFM_API_SECRET = 'your_lastfm_api_secret'
LASTFM_USERNAME = 'your_lastfm_username'
LASTFM_PASSWORD_HASH = pylast.md5('your_lastfm_password')

network = pylast.LastFMNetwork(api_key=LASTFM_API_KEY,
                               api_secret=LASTFM_API_SECRET,
                               username=LASTFM_USERNAME,
                               password_hash=LASTFM_PASSWORD_HASH)

try:
    recent_tracks = network.get_user(LASTFM_USERNAME).get_recent_tracks(limit=1)
    if recent_tracks:
        track = recent_tracks[0].track
        artist_name = track.get_artist().get_name()
        track_name = track.get_title()

        print(f"Currently playing: {track_name} by {artist_name}")

        tags = track.get_top_tags()

        if tags:
            genre = tags[0].item.name
            print(f"Genre: {genre}")
        else:
            print("No genre information found for this track.")
    else:
        print("No recent tracks found for the user.")
except pylast.WSError as e:
    print(f"Error occurred: {e}")
