import os

from twitter.api import TwitterAPI
from twitter.utils import Utils


class Application(TwitterAPI):  # application.py
    """API 'application/'
    レートリミットの情報を取り扱うエンドポイント．
    * GET application/rate_limit_status レートリミット設定と使用状況を取得する。
    """

    def __init__(self, consumer_key: str, consumer_secret: str, access_token: str, access_secret: str):
        super().__init__(consumer_key, consumer_secret, access_token, access_secret)
        self.GET = Application._GET(self.api)
        self.POST = Application._POST(self.api)

    class _GET:
        def __init__(self, api):
            self.method = 'GET'
            self.api = api

        def rate_limit_status(self, params={}):
            """ Return the current rate limits for endpoints you can set as params(like "account,friends")
            * detail:
                ja: 指定したリソース群に属しているメソッドの現在のレート制限を取得します。
                    バージョン1.1 の各API リソースは、そのメソッドのドキュメントに示されている“リソース群(resource family)”に属しています。 通常は、GETもしくはPUTの後ろにある最初のコンポーネントパスから、メソッドの属するリソース群を判別することができます。
                    このメソッドでは、resourcesパラメータで指定したリソース群に属するメソッドの一覧、現在の速度制限時間枠内における各リソースの残り使用回数、現在の速度制限時間枠がリセットされる時間をUNIXエポック秒で表した値、を返します。 また、現在のアクセストークンやアプリケーション単独認証コンテクストを表すrate_limit_context フィールドも返します。
                    また、このメソッドにパラメータを設定せずにリクエストを発行し、全てのGET メソッドのレート制限マップを取得することができます。 あなたのアプリケーションが少数のメソッドのみを使用している場合、resourcesパラメータにあなたが使用しているリソース群を設定してください。
                    When using app-only auth, this method’s response indicates the app-only auth rate limiting context.
                    詳細については API レート制限 と API レート制限早見表を読んでください。
                en: **Returns the current rate limits for methods belonging to the specified resource families**.
                    Each 1.1 API resource belongs to a “resource family” which is indicated in its method documentation. You can typically determine a method’s resource family from the first component of the path after the resource version.
                    This method responds with a map of methods belonging to the families specified by the resources parameter, the current remaining uses for each of those resources within the current rate limiting window, and its expiration time in epoch time. It also includes a rate_limit_context field that indicates the current access token or application-only authentication context.
                    You may also issue requests to this method without any parameters to receive a map of all rate limited GET methods. If your application only uses a few of methods, please explicitly provide a resources parameter with the specified resource families you work with.
                    When using app-only auth, this method’s response indicates the app-only auth rate limiting context.
                    Read more about API Rate Limiting and review the limits.
            * rate-limit: 180 times / 15 min
            * allowed parameter
                * resources(optional): A comma-separated list of resource families you want to know the current rate limit disposition for. For best performance, only specify the resource families pertinent to your application. See API Rate Limiting for more information.
                ex) {'resouces': 'account,statuses,friends,help'}
            """
            path = 'application/rate_limit_status'
            endpoint = Utils.create_endpoint(path)
            params = {'resources': 'account,application'}
            response = self.api.get(url=endpoint, params=params)
            return response

    class _POST:
        def __init__(self, api):
            self.method = 'POST'
            self.api = api
            # "application/" NO POST method


if __name__ == "__main__":
    api = Application(
        consumer_key=os.environ['TW_CONSUMER_KEY'],
        consumer_secret=os.environ['TW_CONSUMER_SECRET'],
        access_token=os.environ['TW_ACCESS_TOKEN'],
        access_secret=os.environ['TW_ACCESS_SECRET'],
    )
    response = api.GET.rate_limit_status()
