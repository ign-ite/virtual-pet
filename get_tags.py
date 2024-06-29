from lastfmapi import GetGenre

class GetTags:
    def __init__(self):
        pass

    def get_tags(self):
        tags = GetGenre().get_top_tags()
        return tags

