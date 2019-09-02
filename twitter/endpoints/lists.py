import os
import sys

from requests_oauthlib import OAuth1Session

from twitter.api import TwitterAPI
from twitter.utils import Utils


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
        self.GET = self._GET(self.api, self.base_url)
        self.POST = self._POST(self.api, self.base_url)

    # inner class for GET methods
    class _GET:
        def __init__(self, api: OAuth1Session, base_url: str):
            self.method = 'GET'
            self.api = api
            self.base_url = base_url

        def list(self, params={
            'user_id': '',
            'screen_name': 'mathnuko',
            'reverse': False,
        }):
            path = 'lists/list.json'
            endpoint = self.base_url + path
            return self.api.get(endpoint, params=params)

        def members(self):
            path = 'lists/members.json'
            endpoint = self.base_url + path

            # Create params
            params = {}
            return self.api.get(url=endpoint, params=params)

        def members_show(self):
            path = 'lists/members/show.json'
            endpoint = self.base_url + path

            # Create params
            params = {}
            return self.api.get(url=endpoint, params=params)

        def memberships(self):
            path = 'lists/memberships.json'
            endpoint = self.base_url + path

            # Create params
            params = {}
            return self.api.get(url=endpoint, params=params)

        def ownerships(self):
            path = 'lists/ownerships.json'
            endpoint = self.base_url + path

            # Create params
            params = {}
            return self.api.get(url=endpoint, params=params)

        def show(self):
            path = 'lists/show.json'
            endpoint = self.base_url + path

            # Create params
            params = {}
            return self.api.get(url=endpoint, params=params)

        def statuses(self):
            path = 'lists/statuses.json'
            endpoint = self.base_url + path

            # Create params
            params = {}
            return self.api.get(url=endpoint, params=params)

        def subscribers(self):
            path = 'lists/subscribers.json'
            endpoint = self.base_url + path

            # Create params
            params = {}
            return self.api.get(url=endpoint, params=params)

        def subscriptions(self):
            path = 'lists/subscriptions.json'
            endpoint = self.base_url + path

            # Create params
            params = {}
            return self.api.get(url=endpoint, params=params)

    # inner class for POST methods
    class _POST:
        def __init__(self, api: OAuth1Session, base_url: str):
            self.method = 'POST'
            self.api = api
            self.base_url = base_url

        def create(self):
            path = 'lists/create.json'
            endpoint = self.base_url + path

            # Create params
            params = {}
            return self.api.post(url=endpoint, params=params)

        def destroy(self):
            path = 'lists/destroy.json'
            endpoint = self.base_url + path

            # Create params
            params = {}
            return self.api.post(url=endpoint, params=params)

        def members_create(self):
            path = 'lists/members/create.json'
            endpoint = self.base_url + path

            # Create params
            params = {}
            return self.api.post(url=endpoint, params=params)

        def members_create_all(self):
            path = 'lists/members/create_all.json'
            endpoint = self.base_url + path

            # Create params
            params = {}
            return self.api.post(url=endpoint, params=params)

        def members_destroy(self):
            path = 'lists/members/destroy.json'
            endpoint = self.base_url + path

            # Create params
            params = {}
            return self.api.post(url=endpoint, params=params)

        def members_destroy_all(self):
            path = 'lists/members/destroy_all.json'
            endpoint = self.base_url + path

            # Create params
            params = {}
            return self.api.post(url=endpoint, params=params)

        def subscribers_create(self):
            path = 'lists/subscribers/create.json'
            endpoint = self.base_url + path

            # Create params
            params = {}
            return self.api.post(url=endpoint, params=params)

        def subscribers_destroy(self):
            path = 'lists/subscribers/destroy.json'
            endpoint = self.base_url + path

            # Create params
            params = {}
            return self.api.post(url=endpoint, params=params)

        def update(self):
            path = 'lists/update.json'
            endpoint = self.base_url + path

            # Create params
            params = {}
            return self.api.post(url=endpoint, params=params)


if __name__ == "__main__":
    api = Lists(
        consumer_key=os.environ['TW_CONSUMER_KEY'],
        consumer_secret=os.environ['TW_CONSUMER_SECRET'],
        access_token=os.environ['TW_ACCESS_TOKEN'],
        access_secret=os.environ['TW_ACCESS_SECRET'],
    )
