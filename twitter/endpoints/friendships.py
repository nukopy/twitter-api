from twitter_api.api import TwitterAPI
from twitter_api.utils import Utils


class Friendships(TwitterAPI):
    """API 'friendships/'
    * GET friendships/incoming 自分に対してフォローリクエストを送っているユーザーを取得する。
    * GET friendships/lookup 自分と対象ユーザーとの関係を取得する。
    * GET friendships/no_retweets/ids 自分がRT非表示中のユーザーを取得する。
    * GET friendships/outgoing 自分がフォローリクエストを送っているユーザーを取得する。
    * GET friendships/show 2人のユーザーの関係を取得する。
    * POST friendships/create フォローする。
    * POST friendships/destroy フォローを解除する。
    * POST friendships/update リツイート非表示、ツイート通知の設定を更新する。
    """

    def __init__(self, consumer_key: str, consumer_secret: str, access_token: str, access_secret: str):
        super().__init__(consumer_key, consumer_secret, access_token, access_secret)
        self.GET = self._GET(self.api)
        self.POST = self._POST(self.api)

    # inner class for GET methods
    class _GET:
        def __init__(self, api):
            self.method = 'GET'
            self.api = api

    # inner class for POST methods
    class _POST:
        def __init__(self, api):
            self.method = 'POST'
            self.api = api
