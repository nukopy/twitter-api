/import os

from twitter.api import TwitterAPI
from twitter.utils import Utils


class Blocks(TwitterAPI):
    """API 'blocks/'
    ブロック関係のデータを取り扱うエンドポイント
    * GET blocks/ids ブロックしているユーザーを、ユーザーIDで取得する。
    * GET blocks/list ブロックしているユーザーを、ユーザーオブジェクトで取得する。
    * POST blocks/create ブロックを実行する。
    * POST blocks/destroy ブロックを解除する。
    """

    def __init__(self, consumer_key: str, consumer_secret: str, access_token: str, access_secret: str):
        super().__init__(consumer_key, consumer_secret, access_token, access_secret)
        self.GET = self._GET(self.api)
        self.POST = self._POST(self.api)

    class _GET:
        def __init__(self, api):
            self.method = 'GET'
            self.api = api

        def ids(self,
                stringify=True,
                cursor=-1):
            """
            * detail:
                ja: 認証ユーザーがブロックしているユーザーの数値型ユーザーIDの配列を取得します。
                    (重要)このメソッドは、指定したページの分だけ情報が表示されます。
                    つまり、全てのブロック情報を漏れなく取得するには、アプリで複数回のリクエストを実行しなければなりません。 カーソリング動作の詳細についてはUsing cursors to navigate collectionsを参照してください。
                en: Returns an array of numeric user ids the authenticating user is blocking.
                    Important This method is cursored, meaning your app must make multiple requests in order to receive all blocks correctly.
                    See Using cursors to navigate collections for more details on how cursoring works.
            * rate-limit: 15 times / 15 min
            * response-limit: 5000 ids / request
            * allowed parameter
                * stringify_ids(optional): 多くのプログラム環境(ex) JavaScript)では桁サイズが原因でTwitterのIDを使用できません。このオプションを設定すると、数値ではなく文字列としてIDを取得します。 詳細については Twitter IDsを読んでください。
                                        サンプル値: true
                * cursor(semi-optional): 現在のところ、取得するIDが5000を超えると複数のページに分割されます。
                                        クエリ後にアカウント停止中のユーザーがフィルタされるので、取得されるIDの数は必ず5000になる訳ではありません。
                                        cursor が設定されなかった場合、一番最初のページを表す -1 が設定されたと見なされます。
                                        API からの応答には previous_cursorパラメータと next_cursorパラメータが含まれており、
                                        これを使って前後のページを操作できます。詳細情報についてはUsing cursors to navigate collectionsを参照してください。
                                        サンプル値: 12893764510938
            """
            path = 'blocks/ids/'
            endpoint = Utils.create_endpoint(path)
            params = {
                'stringify': stringify,
                'cursor': -1
            }
            response = self.api.get(url=endpoint, params=params)
            return response

        def list(self,
                 include_entities=False,
                 skip_status=True,
                 cursor=-1):
            """ Return block list
            * detail:
                ja: 認証ユーザーがブロックしているユーザーのユーザーオブジェクトを取得します。
                    （重要）このメソッドは、指定したページの分だけ情報が表示されます。
                    つまり、全てのブロック情報を漏れなく取得するには、アプリで複数回のリクエストを実行しなければなりません。 カーソリング動作の詳細についてはUsing cursors to navigate collectionsを参照してください。
                en: Returns a collection of user objects that the authenticating user is blocking.
                    Important This method is cursored, meaning your app must make multiple requests in order to receive all blocks correctly.
                    See Using cursors to navigate collections for more details on how cursoring works.
            * rate-limit: 15 times / 15 min
            * allowed parameter
                * include_entities(optional): falseを設定すると、entitiesノードは含まれません。
                * skip_status(optional): trueかtか1を設定した場合、取得したユーザーオブジェクトにステータス情報は含まれません。
                * cursor(semi-optional): 現在のところ、取得するIDが5000を超えると複数のページに分割されます。
                                        クエリ後にアカウント停止中のユーザーがフィルタされるので、取得されるIDの数は必ず5000になる訳ではありません。
                                        cursor が設定されなかった場合、一番最初のページを表す -1 が設定されたと見なされます。
                                        API からの応答には previous_cursorパラメータと next_cursorパラメータが含まれており、これを使って前後のページを操作できます。詳細情報についてはUsing cursors to navigate collectionsを参照してください。
                                        サンプル値: 12893764510938
            """
            path = 'blocks/list/'
            endpoint = Utils.create_endpoint(path)
            params = {
                'include_entities': include_entities,
                'skip_status': skip_status,
                'cursor': cursor
            }
            response = self.api.get(url=endpoint, params=params)
            return response

    class _POST:
        def __init__(self, api):
            self.method = 'POST'
            self.api = api

        def create(self,
                   screen_name='realnet_yuyasan',
                   user_id='',
                   include_entities=False,
                   skip_status=True):
            """ Block a user
            * detail:
                ja: 指定したユーザーをブロックします。
                    また、ブロックされたユーザーは認証ユーザーのメンションやタイムラインに表示されません (他のユーザーがリツイートしない限り)。
                    フォロー関係や友達関係があった場合、その関係は破棄されます。
                    /version/block/create/:screen_name_or_user_id.formatのURLパターンはまだ使用できますが、非推奨です。 スクリーンネームには数字を使うことができるので 、代わりに screen_name パラメータもしくは user_id パラメータを使用することを推奨します。
                en: Blocks the specified user from following the authenticating user.
                    In addition the blocked user will not show in the authenticating users mentions or timeline (unless retweeted by another user).
                    If a follow or friend relationship exists it is destroyed.
                    The URL pattern /version/block/create/:screen_name_or_user_id.format is still accepted but not recommended. As a sequence of numbers is a valid screen name we recommend using the screen_name or user_id parameter instead.
            * rate-limit: YES, but NOT specified in documents
            * allowed parameter
                * At least 1 of 2 MUST
                    * screen_name(optional): ブロックされるユーザーのスクリーンネーム（like "@mathnuko", screen_name -> "mathnuko"）。
                                    スクリーンネームとユーザーIDが同じ場合に、どちらを指定しているのか明確にするために使います。
                                    サンプル値: noradio(@ 以降の文字列が screen_name)
                    * user_id(optional): ブロックされるユーザーのユーザーID。ユーザーIDとスクリーンネームが同じ場合に、どちらを指定しているのか明確にするために使います。
                                    サンプル値: 12345
                * include_entities(optional): falseを設定すると、entitiesノードは含まれません。
                * skip_status(optional): trueかtか1を設定した場合、取得したユーザーオブジェクトにステータス情報は含まれません。
            """
            path = 'blocks/create/'
            endpoint = Utils.create_endpoint(path)
            params = {
                'screen_name': screen_name,
                'user_id': user_id,
                'include_entities': include_entities,
                'skip_status': skip_status,
            }
            response = self.api.post(url=endpoint, params=params)
            return response

        def destroy(self,
                    screen_name='realnet_yuyasan',
                    user_id='',
                    include_entities=False,
                    skip_status=True):
            """ Unblock a user
            * detail:
                ja: IDパラメータで指定したユーザーのブロックを解除します。
                    成功した場合、ブロックを解除したユーザーの情報がリクエストした形式で返されます。
                    ブロックする前の関係性までは復元されません。
                en: Un-blocks the user specified in the ID parameter for the authenticating user.
                    Returns the un-blocked user in the requested format when successful. If relationships existed before the block was instated, they will not be restored.
            * rate-limit: YES, but NOT specified in documents
            * allowed parameter
                * At least 1 of 2 MUST
                    * screen_name(optional): ブロックされるユーザーのスクリーンネーム（like "@mathnuko", screen_name -> "mathnuko"）。
                                    スクリーンネームとユーザーIDが同じ場合に、どちらを指定しているのか明確にするために使います。
                                    サンプル値: noradio(@ 以降の文字列が screen_name)
                    * user_id(optional): ブロックされるユーザーのユーザーID。ユーザーIDとスクリーンネームが同じ場合に、どちらを指定しているのか明確にするために使います。
                                    サンプル値: 12345
                * include_entities(optional): falseを設定すると、entitiesノードは含まれません。
                * skip_status(optional): trueかtか1を設定した場合、取得したユーザーオブジェクトにステータス情報は含まれません。

            """
            path = 'blocks/destroy/'
            endpoint = Utils.create_endpoint(path)
            params = params = {
                'screen_name': screen_name,
                'user_id': user_id,
                'include_entities': include_entities,
                'skip_status': skip_status,
            }
            response = self.api.post(url=endpoint, params=params)
            return response


if __name__ == "__main__":
    api = Blocks(
        consumer_key=os.environ['TW_CONSUMER_KEY'],
        consumer_secret=os.environ['TW_CONSUMER_SECRET'],
        access_token=os.environ['TW_ACCESS_TOKEN'],
        access_secret=os.environ['TW_ACCESS_SECRET'],
    )

    # dump
    segment = 'blocks'
    # Utils.dump2json(segment, 'GET_ids', api.GET.ids().json())
    # Utils.dump2json(segment, 'GET_list_DEFAULT', api.GET.ids().json())
    # Utils.dump2json(
    #     segment,
    #     'GET_list_PARAMS_entities_status',
    #     api.GET.list(
    #         include_entities=True,
    #         skip_status=False,
    #         cursor=-1
    #     ).json()
    # )
    Utils.dump2json(
        segment,
        'POST_create_DEFAULT',
        api.POST.create().json()
    )
    Utils.dump2json(
        segment,
        'POST_destroy_DEFAULT',
        api.POST.destroy().json()
    )
