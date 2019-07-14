# Twitter API
from requests_oauthlib import OAuth1Session
from datetime import datetime
import os
import tweepy

from .utils import Utils
# import sys;sys.path.append('/Users/okuwaki/Projects/AtCoderStream/AtCoderStream/lib/twitter_api')
API_VERSION = '1.1'
BASE_URL = f'https://api.twitter.com/{API_VERSION}/'


class TwitterAPI:
    def __init__(self,
                 consumer_key: str = None,
                 consumer_secret: str = None,
                 access_token: str = None,
                 access_secret: str = None,
                 application_only_auth: bool = False,
                 api_host: str = 'https://api.twitter.com/',
                 api_version: str = '1.1',
                 cache: str = None,
                 ):
        """[summary]

        Keyword Arguments:
            consumer_key {str} -- [description] (default: {None})
            consumer_secret {str} -- [description] (default: {None})
            access_token {str} -- [description] (default: {None})
            access_secret {str} -- [description] (default: {None})
            application_only_auth {bool} -- [In general, endpoints related to specific user information will require OAuth (Application-user) authentication, and endpoints related to retrieving **publicly available** information will require OAuth2 (bearer token) or Basic Auth (for Enterprise data APIs).] (default: {False})
                * specific user information: OAuth1 (Application-user) authentication
                * publicly available: OAuth 2(bearer token) or Basic authentication
            api_host {str} -- [description] (default: {'https://api.twitter.com/'})
            api_version {str} -- [description] (default: {'1.1'})
            cache {str} -- [description] (default: {None})
        """
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_secret = access_secret
        self.application_only_auth = application_only_auth
        self.api_host = api_host
        self.api_version = api_version
        self.cache = cache

        # API authentication & authorization
        self.api = None


# DONE list
# * Account(TwitterAPI): account.py
# * Application(TwitterAPI): application.py
# * Blocks(TwitterAPI): blocks.py
# * Collections: NOT implemented


class DirectMessages(TwitterAPI):
    """API 'direct_messages'
    ダイレクトメッセージのデータを取り扱うエンドポイント
    * GET direct_messages 受信したダイレクトメッセージを取得する。
    * GET direct_messages/sent 送信したダイレクトメッセージを取得する。
    * GET direct_messages/show 個別のダイレクトメッセージの内容を取得する。
    * POST direct_messages/destroy ダイレクトメッセージを削除する。
    * POST direct_messages/new ダイレクトメッセージを送信する。
    """
    pass


class Favorites(TwitterAPI):
    """API 'favorites/'
    お気に入り関係のデータを取り扱うエンドポイント
    * GET favorites/list 対象ユーザーがお気に入りに登録したツイートの一覧を取得する。
    * POST favorites/create 対象ツイートにいいねを付ける。
    * POST favorites/destroy 対象ツイートのいいねを取り消す。
    """
    pass


class Followers(TwitterAPI):
    """API 'followers/'
    フォロワー関係のデータを取り扱うエンドポイント．
    * GET followers/ids 対象ユーザーのフォロワーを、IDの一覧で取得する。
    * GET followers/list 対象ユーザーのフォロワーを、オブジェクトの一覧で取得する。
    """
    pass


class Friends(TwitterAPI):
    """API 'friends/'
    フォロー関係のデータを取り扱うエンドポイント．
    * GET friends/ids 対象ユーザーがフォローしているユーザーを、IDの一覧で取得する。
    * GET friends/list 対象ユーザーがフォローしているユーザーを、オブジェクトの一覧で取得する。
    """
    pass


class Friendships(TwitterAPI):
    """API 'friendships/'
    * GET friendships/incoming 自分に対してフォローリクエストを送っているユーザーを取得する。
    * GET friendships/lookup 自分と対象ユーザーとの関係を取得する。
    * GET friendships/no_retweets/ids 自分がRT非表示中のユーザーを取得する。
    * GET friendships/outgoing 自分がフォローリクエストを送っているユーザーを取得する。
    * GET friendships/show 2人のユーザーの関係を取得する。
    * POST friendships/create フォローする。
    * POST friendships/destroy フォローを解除する。
    * POST friendships/update リツイート非表示、ツイート通知の設定を更新する。
    """
    pass


class Geo(TwitterAPI):
    """API 'geo/'
    場所や位置座標の情報を取り扱うエンドポイント．
    * GET geo/id/:place_id 場所の情報を取得する。
    * GET geo/reverse_geocode 緯度、経度から場所の情報を取得する。
    * GET geo/search 場所を検索する。
    """
    pass


class Help(TwitterAPI):
    """API 'help/'
    Twitterの規約関係のデータを取り扱うエンドポイント．
    * GET help/configuration Twitterの内部設定を取得する。
    * GET help/languages Twitterが対応している言語の一覧を取得する。
    * GET help/privacy Twitterのプライバシーポリシーを取得する。
    * GET help/tos Twitterのサービス利用規約を取得する。
    """
    pass


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
    pass


class Media(TwitterAPI):
    """API 'media/'
    メディアアップロードをするエンドポイント．
    * POST media/upload 画像をアップロードする。
    * POST media/upload (APPEND) 動画のアップロードを実行する。
    * POST media/upload (FINALIZE) 動画のアップロードを完了する。
    * POST media/upload (INIT) 動画のアップロードを準備する。
    """
    pass


class Mutes(TwitterAPI):
    """API 'mutes/'
    ミュート関係のデータを取り扱うエンドポイント．
    * GET mutes/users/ids 自分がミュートしているユーザーを、ユーザーIDの一覧で取得する。
    * GET mutes/users/list 自分がミュートしているユーザーを、オブジェクトの一覧で取得する。
    * POST mutes/users/create ミュートを実行する。
    * POST mutes/users/destroy ミュートを解除する
    """
    pass


class SavedSearches(TwitterAPI):
    """API 'saved_searches/'
    検索メモ関係のデータを取り扱うエンドポイント．
    * GET saved_searches/list 検索メモを一覧で取得する。
    * GET saved_searches/show/:id 検索メモを個別に取得する。
    * POST saved_searches/create 検索メモを保存する。
    * POST saved_searches/destroy/:id 検索メモを削除する。
    """
    pass


class Search(TwitterAPI):
    """API 'search/'
    ツイートの検索APIを利用できます。
    * GET search/tweets ツイートを検索する。
    """
    pass


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
    pass


class Trends(TwitterAPI):
    """API 'trends/'
    トレンドの情報を取り扱うエンドポイント．
    * GET trends/available トレンドの集計対象となっている地域の一覧を取得する。
    * GET trends/closest 位置座標からWOEIDを取得する。
    * GET trends/place トレンドワードを取得する。
    """
    pass


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
    pass


if __name__ == "__main__":
    api = TwitterAPI(
        consumer_key=os.environ['TW_CONSUMER_KEY'],
        consumer_secret=os.environ['TW_CONSUMER_SECRET'],
        access_token=os.environ['TW_ACCESS_TOKEN'],
        access_secret=os.environ['TW_ACCESS_SECRET'],
    )
