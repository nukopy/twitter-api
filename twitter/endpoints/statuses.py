from twitter_api.api import TwitterAPI
from twitter_api.utils import Utils


class Statuses(TwitterAPI):
    """API 'statuses/'
    ツイート関係のデータを取り扱うエンドポイント．
    * GET statuses/home_timeline ホームタイムラインを取得する。
    * GET statuses/lookup ツイートを任意の数だけ取得する。
    * GET statuses/mentions_timeline メンションタイムラインを取得する。
    * GET statuses/oembed 対象ツイートの埋め込み用コードを取得する。
    * GET statuses/retweeters/ids 対象ツイートをリツイートしたユーザーを、ユーザーIDの一覧で取得する。
    * GET statuses/retweets/:id 対象ツイートをリツイートしたユーザーを、オブジェクトの一覧で取得する。
    * GET statuses/retweets_of_me リツイートされたツイートの一覧を取得する。
    * GET statuses/show/:id ツイートを個別に取得する。
    * GET statuses/user_timeline ユーザータイムラインを取得する。
    * POST statuses/destroy/:id ツイートを削除する。
    * POST statuses/retweet/:id リツイートを実行する。
    * POST statuses/unretweet/:id リツイートを取り消す。
    * POST statuses/update ツイートを投稿する。
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
