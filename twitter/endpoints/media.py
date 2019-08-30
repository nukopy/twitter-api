from twitter_api.api import TwitterAPI
from twitter_api.utils import Utils


class Media(TwitterAPI):
    """API 'media/'
    メディアアップロードをするエンドポイント．
    * POST media/upload 画像をアップロードする。
    * POST media/upload (APPEND) 動画のアップロードを実行する。
    * POST media/upload (FINALIZE) 動画のアップロードを完了する。
    * POST media/upload (INIT) 動画のアップロードを準備する。
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
