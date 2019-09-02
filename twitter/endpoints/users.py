import os
from typing import List, Union

from requests_oauthlib import OAuth1Session

from twitter.api import TwitterAPI
from twitter.utils import Utils


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
        self.GET = self._GET(self.api, self.base_url)
        self.POST = self._POST(self.api, self.base_url)

    # inner class for GET methods
    class _GET:
        def __init__(self, api: OAuth1Session, base_url: str):
            self.method = 'GET'
            self.api = api
            self.base_url = base_url

        def lookup(
            self,
            user_id: Union[str, int] = None,
            screen_name: str = None,
            users: List[str] = None,
            include_entities: bool = True,
            #
            user_id_list: List[Union[str, int]] = [],
            screen_name_list: List[str] = [],
        ):
            """lookup
            * detail:
              ja: 任意の数だけ指定したユーザの情報を取得するエンドポイント．一度に 100 件まで取得可能．
            * rate-limit: 900 times / 15 min
            """
            path = 'users/lookup.json'
            endpoint = self.base_url + path

            # Create params
            # Check arguments
            params_list = [
                user_id,
                screen_name,
                user_id_list,
                screen_name_list
            ]
            param_num = sum([bool(param) for param in params_list])
            if param_num == 1:
                # Only 1 of params(user_id, screen_name) is needed
                params = {
                    'include_entities': include_entities
                }

                if user_id:
                    params['user_id'] = user_id
                elif screen_name:
                    params['screen_name'] = screen_name
                elif user_id_list:
                    # user_id のリストをカンマ区切りの文字列へ変換
                    params['user_id'] = ','.join(user_id_list)
                elif screen_name_list:
                    # screen_name のリストをカンマ区切りの文字列へ変換
                    params['screen_name'] = ','.join(screen_name_list)

                # request
                return self.api.get(url=endpoint, params=params)
            else:
                raise Exception(
                    '1 of 4(user_id, screen_name, user_id_list, screen_name_list),  must be assigned.'
                )

        def profile_banner(self):
            path = 'users/profile_banner.json'
            endpoint = self.base_url + path
            return self.api.get(url=endpoint)

        def search(self):
            path = 'users/search.json'
            endpoint = self.base_url + path
            return self.api.get(url=endpoint)

        def show(self):
            path = 'users/show.json'
            endpoint = self.base_url + path
            return self.api.get(url=endpoint)

        def suggestions(self):
            path = 'users/suggestions.json'
            endpoint = self.base_url + path
            return self.api.get(url=endpoint)

        def suggestions_slug(self, slug: str):
            path = f'users/suggestions/{slug}.json'
            endpoint = self.base_url + path
            return self.api.get(url=endpoint)

        def suggestions_slug_members(self, slug: str):
            path = f'users/suggestions/{slug}/members.json'
            endpoint = self.base_url + path
            return self.api.get(url=endpoint)

    # inner class for POST methods

    class _POST:
        def __init__(self, api: OAuth1Session, base_url: str):
            self.method = 'POST'
            self.api = api
            self.base_url = base_url

        def report_spam(self):
            path = 'users/report_spam.json'
            endpoint = self.base_url + path
            return self.api.post(url=endpoint)


if __name__ == "__main__":
    users = Users(
        consumer_key=os.environ['TW_CONSUMER_KEY'],
        consumer_secret=os.environ['TW_CONSUMER_SECRET'],
        access_token=os.environ['TW_ACCESS_TOKEN'],
        access_secret=os.environ['TW_ACCESS_SECRET'],
    )
