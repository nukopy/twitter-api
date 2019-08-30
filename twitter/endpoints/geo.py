from twitter_api.api import TwitterAPI
from twitter_api.utils import Utils


class Geo(TwitterAPI):
    """API 'geo/'
    場所や位置座標の情報を取り扱うエンドポイント．
    * GET geo/id/:place_id 場所の情報を取得する。
    * GET geo/reverse_geocode 緯度、経度から場所の情報を取得する。
    * GET geo/search 場所を検索する。
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
