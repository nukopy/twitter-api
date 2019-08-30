import os
from twitter.api import TwitterAPI
from twitter.utils import Utils
import sys


class Lists(TwitterAPI):
    """API 'lists/'
    リスト関係のデータを取り扱うエンドポイント．
    * GET lists/list 対象ユーザーのリスト一覧を取得する。
    * GET lists/members 対象のリストにメンバー(発言者)として加えられているユーザーの一覧を取得する。
    * GET lists/members/show 対象のリストに、対象のユーザーがメンバーとして加わっているか否かを確認する。
    * GET lists/memberships lists/members/memberships(GETメソッド)は、対象ユーザーが、メンバー(発言者)として加えられているリストの一覧を取得するエンドポイントです。
    * GET lists/ownerships 対象ユーザーが作成したリストの一覧を取得する。
    * GET lists/show 対象のリストを取得する。
    * GET lists/statuses リストのタイムラインを取得する。
    * GET lists/subscribers リストの購読者を取得する。
    * GET lists/subscriptions ユーザーが購読しているリストを取得する。
    * POST lists/create リストを作成する。
    * POST lists/destroy リストを削除する。
    * POST lists/members/create リストにメンバーを追加する。
    * POST lists/members/create_all リストに複数のメンバーを追加する。
    * POST lists/members/destroy リストからメンバーを削除する。
    * POST lists/members/destroy_all リストから複数のメンバーを削除する。
    * POST lists/subscribers/create リストを保存する。
    * POST lists/subscribers/destroy リストの購読を取り消す。
    * POST lists/update リストの設定を更新する。
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

        def list(self, params={
            'user_id': '',
            'screen_name': 'mathnuko',
            'reverse': False,
        }):
            endpoint = Utils.create_endpoint('lists/list')
            return self.api.get(endpoint, params=params)

        def members(self):
            endpoint = Utils.create_endpoint('lists/members')

        def members_show(self):
            endpoint = Utils.create_endpoint('lists/members/show')

        def memberships(self):
            endpoint = Utils.create_endpoint('lists/memberships')

        def ownerships(self):
            endpoint = Utils.create_endpoint('lists/ownerships')

        def show(self):
            endpoint = Utils.create_endpoint('lists/show')

        def statuses(self):
            endpoint = Utils.create_endpoint('lists/statuses')

        def subscribers(self):
            endpoint = Utils.create_endpoint('lists/subscribers')

        def subscriptions(self):
            endpoint = Utils.create_endpoint('lists/subscriptions')

    # inner class for POST methods

    class _POST:
        def __init__(self, api):
            self.method = 'POST'
            self.api = api

        def create(self):
            endpoint = Utils.create_endpoint('lists/create')

        def destroy(self):
            endpoint = Utils.create_endpoint('lists/destroy')

        def members_create(self):
            endpoint = Utils.create_endpoint('lists/members/create')

        def members_create_all(self):
            endpoint = Utils.create_endpoint('lists/members/create_all')

        def members_destroy(self):
            endpoint = Utils.create_endpoint('lists/members/destroy')

        def members_destroy_all(self):
            endpoint = Utils.create_endpoint('lists/members/destroy_all')

        def subscribers_create(self):
            endpoint = Utils.create_endpoint('lists/subscribers/create')

        def subscribers_destroy(self):
            endpoint = Utils.create_endpoint('lists/subscribers/destroy')

        def update(self):
            endpoint = Utils.create_endpoint('lists/update')


if __name__ == "__main__":
    import sys
    sys.path.append(
        '/Users/okuwaki/Projects/AtCoderStream/AtCoderStream/lib/twitter_api'
    )
    api = Lists(
        consumer_key=os.environ['TW_CONSUMER_KEY'],
        consumer_secret=os.environ['TW_CONSUMER_SECRET'],
        access_token=os.environ['TW_ACCESS_TOKEN'],
        access_secret=os.environ['TW_ACCESS_SECRET'],
    )
    res = api.list()
