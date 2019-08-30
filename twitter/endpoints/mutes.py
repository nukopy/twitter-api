from twitter_api.api import TwitterAPI
from twitter_api.utils import Utils


class Mutes(TwitterAPI):
    """API 'mutes/'
    ミュート関係のデータを取り扱うエンドポイント．
    * GET mutes/users/ids 自分がミュートしているユーザーを、ユーザーIDの一覧で取得する。
    * GET mutes/users/list 自分がミュートしているユーザーを、オブジェクトの一覧で取得する。
    * POST mutes/users/create ミュートを実行する。
    * POST mutes/users/destroy ミュートを解除する
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
