# Twitter API
from requests_oauthlib import OAuth1Session
from datetime import datetime
import os
import tweepy

from .utils import Utils
# import sys;sys.path.append('/Users/okuwaki/Projects/AtCoderStream/AtCoderStream/lib/twitter_api')


class TwitterAPI:
    def __init__(self, consumer_key: str, consumer_secret: str, access_token: str, access_secret: str):
        print('TwitterAPI instance initialized.\n')
        self.api = OAuth1Session(
            client_key=consumer_key,
            client_secret=consumer_secret,
            resource_owner_key=access_token,
            resource_owner_secret=access_secret
        )


class Account(TwitterAPI):  # account.py
    pass


class Application(TwitterAPI):  # application.py
    """API 'application/'
    レートリミットの情報を取り扱うエンドポイント．
    * GET application/rate_limit_status レートリミット設定と使用状況を取得する。
    """
    pass


class Blocks(TwitterAPI):
    """API 'blocks/'
    ブロック関係のデータを取り扱うエンドポイント
    * GET blocks/ids ブロックしているユーザーを、ユーザーIDで取得する。
    * GET blocks/list ブロックしているユーザーを、ユーザーオブジェクトで取得する。
    * POST blocks/create ブロックを実行する。
    * POST blocks/destroy ブロックを解除する。
    """
    pass


class Collections(TwitterAPI):
    pass


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
    """API 'mutes/'
    ミュート関係のデータを取り扱うエンドポイント．
    * GET mutes/users/ids 自分がミュートしているユーザーを、ユーザーIDの一覧で取得する。
    * GET mutes/users/list 自分がミュートしているユーザーを、オブジェクトの一覧で取得する。
    * POST mutes/users/create ミュートを実行する。
    * POST mutes/users/destroy ミュートを解除する
    """
    pass


class Mutes(TwitterAPI):
    """API 'media/'
    メディアアップロードをするエンドポイント．
    * POST media/upload 画像をアップロードする。
    * POST media/upload (APPEND) 動画のアップロードを実行する。
    * POST media/upload (FINALIZE) 動画のアップロードを完了する。
    * POST media/upload (INIT) 動画のアップロードを準備する。
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
