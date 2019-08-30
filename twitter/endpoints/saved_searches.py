from twitter_api.api import TwitterAPI
from twitter_api.utils import Utils


class SavedSearches(TwitterAPI):
    """API 'saved_searches/'
    検索メモ関係のデータを取り扱うエンドポイント．
    * GET saved_searches/list 検索メモを一覧で取得する。
    * GET saved_searches/show/:id 検索メモを個別に取得する。
    * POST saved_searches/create 検索メモを保存する。
    * POST saved_searches/destroy/:id 検索メモを削除する。
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
