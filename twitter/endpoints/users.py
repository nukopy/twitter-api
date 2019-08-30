from twitter_api.api import TwitterAPI
from twitter_api.utils import Utils


class Users(TwitterAPI):
    """API 'users/'
    ユーザープロフィールに関係するデータを取り扱うエンドポイント．
    * GET users/lookup 複数のユーザーの情報を取得する。
    * GET users/profile_banner プロフィールのバナー画像を取得する。
    * GET users/search ユーザーを検索する。
    * GET users/show ユーザーのプロフィールを取得する。
    * GET users/suggestions サジェストのカテゴリを取得する。
    * GET users/suggestions/:slug おすすめユーザーを取得する。
    * GET users/suggestions/:slug/members おすすめユーザーをツイート付きで取得する。
    * POST users/report_spam スパム報告を実行する。
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
