from twitter_api.api import TwitterAPI
from twitter_api.utils import Utils


from twitter_api.api import TwitterAPI
from twitter_api.utils import Utils


class Trends(TwitterAPI):
    """API 'trends/'
    トレンドの情報を取り扱うエンドポイント．
    * GET trends/available トレンドの集計対象となっている地域の一覧を取得する。
    * GET trends/closest 位置座標からWOEIDを取得する。
    * GET trends/place トレンドワードを取得する。
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
