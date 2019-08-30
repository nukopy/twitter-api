from twitter_api.api import TwitterAPI
from twitter_api.utils import Utils


class DirectMessages(TwitterAPI):
    """API 'direct_messages'
    ダイレクトメッセージのデータを取り扱うエンドポイント
    * GET direct_messages 受信したダイレクトメッセージを取得する。
    * GET direct_messages/sent 送信したダイレクトメッセージを取得する。
    * GET direct_messages/show 個別のダイレクトメッセージの内容を取得する。
    * POST direct_messages/destroy ダイレクトメッセージを削除する。
    * POST direct_messages/new ダイレクトメッセージを送信する。
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
