from twitter_api.api import TwitterAPI
from twitter_api.utils import Utils


class Help(TwitterAPI):
    """API 'help/'
    Twitterの規約関係のデータを取り扱うエンドポイント．
    * GET help/configuration Twitterの内部設定を取得する。
    * GET help/languages Twitterが対応している言語の一覧を取得する。
    * GET help/privacy Twitterのプライバシーポリシーを取得する。
    * GET help/tos Twitterのサービス利用規約を取得する。
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
