# Twitter API
from requests_oauthlib import OAuth1Session
from datetime import datetime
import os
import tweepy

from .utils import Utils
# import sys;sys.path.append('/Users/okuwaki/Projects/AtCoderStream/AtCoderStream/lib/twitter_api')
API_VERSION = '1.1'
BASE_URL = f'https://api.twitter.com/{API_VERSION}/'


class TwitterAPI:
    def __init__(self,
                 consumer_key: str = None,
                 consumer_secret: str = None,
                 access_token: str = None,
                 access_secret: str = None,
                 application_only_auth: bool = False,
                 api_host: str = 'https://api.twitter.com/',
                 api_version: str = '1.1',
                 cache: str = None,
                 ):
        """[summary]

        Keyword Arguments:
            consumer_key {str} -- [description] (default: {None})
            consumer_secret {str} -- [description] (default: {None})
            access_token {str} -- [description] (default: {None})
            access_secret {str} -- [description] (default: {None})
            application_only_auth {bool} -- [In general, endpoints related to specific user information will require OAuth (Application-user) authentication, and endpoints related to retrieving **publicly available** information will require OAuth2 (bearer token) or Basic Auth (for Enterprise data APIs).] (default: {False})
                * specific user information: OAuth1 (Application-user) authentication
                * publicly available: OAuth 2(bearer token) or Basic authentication
            api_host {str} -- [description] (default: {'https://api.twitter.com/'})
            api_version {str} -- [description] (default: {'1.1'})
            cache {str} -- [description] (default: {None})
        """
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_secret = access_secret
        self.application_only_auth = application_only_auth
        self.api_host = api_host
        self.api_version = api_version
        self.cache = cache

        # API authentication & authorization
        self.api = None


# API endpoint list
# 全 18 API

# * Account(TwitterAPI): account.py
# * Application(TwitterAPI): application.py
# * Blocks(TwitterAPI): blocks.py
# * Collections: NOT implemented
# * DirectMessages: direct_messages.py

# * Favorites: favorites.py
# * Followers: followers.py
# * Friendships: friendships.py
# * Geo: geo.py
# * Help: help.py

# * Lists: lists.py
# * Media: media.py
# * Mutes: mutes.py
# * SavedSearches: saved_searches.py
# * Search: search.py

# * Statuses: statuses.py
# * Trends: trends.py
# * Users: users.py


if __name__ == "__main__":
    api = TwitterAPI(
        consumer_key=os.environ['TW_CONSUMER_KEY'],
        consumer_secret=os.environ['TW_CONSUMER_SECRET'],
        access_token=os.environ['TW_ACCESS_TOKEN'],
        access_secret=os.environ['TW_ACCESS_SECRET'],
    )
