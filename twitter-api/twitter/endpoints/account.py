import os

from twitter.api import TwitterAPI
from twitter.utils import Utils


class Account(TwitterAPI):
    """API 'account/'
    アカウント設定のデータを取り扱うエンドポイント．
    自分のアカウントを制御できる．
    * GET account/settings 認証ユーザーのアカウント設定を取得する。
    * GET account/verify_credentials 認証ユーザーのアカウントが有効な状態か確認する。
    * POST account/remove_profile_banner バナー画像を削除する。
    * POST account/settings アカウントの設定を更新する。
    * POST account/update_profile プロフィールを更新する。
    * POST account/update_profile_background_image プロフィールの背景画像を更新する。
    * POST account/update_profile_banner プロフィールのバナー画像を更新する。
    * POST account/update_profile_image プロフィールのアイコン画像を更新する。
    """

    def __init__(self, consumer_key: str, consumer_secret: str, access_token: str, access_secret: str):
        super().__init__(consumer_key, consumer_secret, access_token, access_secret)
        self.GET = Account._GET(self.api)
        self.POST = Account._POST(self.api)

    # inner class for GET methods
    class _GET:
        def __init__(self, api):
            self.method = 'GET'
            self.api = api

        def settings(self):
            """settings
            * detail:
                ja: 認証ユーザーの設定(トレンド情報、地理情報、睡眠時間情報も含みます)を取得します。
                en: Returns settings (including current trend, geo and sleep time information) for the authenticating user.
            * rate-limit: 15 times / 15 min
            * allowed parameter: None
            """
            path = 'account/settings'
            endpoint = Utils.create_endpoint(path)
            response = self.api.get(url=endpoint)
            return response

        def verify_credentials(self):
            """verify_credentials
            * detail:
                ja: 認証に成功した場合、HTTP 200 OKのレスポンスコードと認証要求したユーザーの情報(settings と同じ)を返します。; 認証に失敗した場合、401 のステータスコードとエラーメッセージを返します。 このメソッドを使って、指定したユーザーの資格情報が有効かどうかテストします。
                en: Returns an HTTP 200 OK response code and a representation of the requesting user if authentication was successful; returns a 401 status code and an error message if not. Use this method to test if supplied user credentials are valid.
            * rate-limit: 75 times / 15 min
            * allowed parameter: None
            """
            path = 'account/verify_credentials'
            endpoint = Utils.create_endpoint(path)
            return self.api.get(url=endpoint)

    # inner class for POST methods
    class _POST:
        def __init__(self, api):
            self.method = 'POST'
            self.api = api

        def remove_profile_banner(self):
            """ remove_profile_banner
            * detail:
                ja: アップロードした認証ユーザーのプロフィールバナーを削除します。成功した場合は HTTP 200 が返ります。
                en: Removes the uploaded profile banner for the authenticating user. Returns HTTP 200 upon success.
            * rate-limit:  times /  min
            * allowed parameter: None
            """
            path = 'account/remove_profile_banner'
            endpoint = Utils.create_endpoint(path)
            return self.api.post(url=endpoint)

        def settings(self):  # GET と POST で同じ名前
            """ settings
            * detail:
                ja: 認証ユーザーの設定を更新します。
                en: Updates the authenticating user’s settings.
            * rate-limit:  times /  min
            * allowed parameter
                * sleep_time_enabled(optional): 
                * start_sleep_time(optional): 
                * end_sleep_time(optional): 
                * time_zone(optional): 
                * trend_location(optional): 
                * allow_contributor_request(optional): 
                * lang(optional): it, en, ja, es, etc...
            """
            path = 'account/settings'
            endpoint = Utils.create_endpoint(path)

        def update_profile(self):
            """
            * detail:
                ja: 自分の設定ページの「アカウント」（"Account"）タブ配下でユーザーが設定可能な値を設定します．
                    指定したパラメータのみが更新されます。
                en: Sets some values that users are able to set under the “Account” tab of their settings page.
                    Only the parameters specified will be updated.
            * rate-limit:  times /  min
            * allowed parameter
                * name(optional): このプロフィールに関連付けるフルネーム。最大20文字。
                * url(optional): このプロフィールに関連付けるURL。“http://”が付いていない場合は自動的に付けられます。最大100文字
                * location(optional): このアカウントのユーザーがいる場所を説明する都市名や国名。この値は、正規化やジオコードに対応したものではありません。最大30文字。
                * description(optional): アカウント保持ユーザーの説明。最大160文字。
                * profile_link_color(optional): 認証ユーザーのtwitter.comプロフィールページで使われているリンクの配色を制御するヘックス値を設定します。 これには有効な16進の値を設定しなければならず、3文字か6文字になります (例: F00 や FF0000)。
                * include_entities(optional): falseを設定すると、 entitiesノードは含まれません。
                * skip_status(optional): trueやt や 1を設定した場合、ユーザーオブジェクトにステータス情報は含まれません。
            """
            path = 'account/update_profile'
            endpoint = Utils.create_endpoint(path)

        def update_profile_background_image(self):
            """ update_profile_background_image
            * detail:
                ja: 認証ユーザーのプロフィールの背景画像を更新します。
                    このメソッドはを使って、プロフィールの背景画を有効もしくは無効にすることもできます。
                    各パラメータは任意で設定するものですが、
                    リクエストする際には少なくとも image, tile , useのうちいずれか一つは設定しなければなりません。
                en: Updates the authenticating user’s profile background image.
                    This method can also be used to enable or disable the profile background image.
                    Although each parameter is marked as optional,
                    at least one of "image", "tile" or "use" must be provided when making this request.
            * rate-limit:  times /  min
            * allowed parameter
                * At least 1 of 3 MUST
                    * image(optional): 
                    * tile(optional): 
                    * use(optional): 
                * include_entitles: 
                * skip_status: 
            """
            path = 'account/update_profile_background_image'
            endpoint = Utils.create_endpoint(path)

        def update_profile_banner(self):
            """ update_profile_banner
            * detail:
                ja: 認証ユーザーのプロフィールバナーをアップロードします。
                    For best results, upload an profile_banner_url node in their "Users" objects. sizing variationsの詳細情報についてはUser Profile Images and Banners とGET users / profile_bannerで見ることができます。
                    プロフィールバナー画像は非同期で処理されます。 The profile_banner_url and its variant sizes will not necessary be available directly after upload.
                en: Uploads a profile banner on behalf of the authenticating user.
                    For best results, upload an profile_banner_url node in their "Users" objects. More information about sizing variations can be found in User Profile Images and Banners and GET users / profile_banner.
                    Profile banner images are processed asynchronously. The profile_banner_url and its variant sizes will not necessary be available directly after upload.
                HTTP response code:
                    * code(s): meaning
                    * 200, 201, 202: Profile banner image succesfully uploaded
                    * 400: Either an image was not provided or the image data could not be processed.
                    * 422: The image could not be resized or is too large.
            * rate-limit:  times /  min
            * allowed parameter
                * banner(MUST): image
                * width(optional): 
                * height(optional): 
                * offset_left(optional): 
                * offset_top(optional):
                CAUTION: height, width, offset_left, offset_top の各パラメータのうちいずれか一つを設定した場合、全てのサイズパラメータを設定しなければなりません。
            """
            path = 'account/update_profile_banner'
            endpoint = Utils.create_endpoint(path)

        def update_profile_image(self):
            """
            * detail:
                ja: 認証ユーザーのプロフィール画像を更新します。このメソッドでは画像へのURLではなくRAWマルチパートデータを使用するので注意してください。
                    このメソッドでは非同期でファイルのアップデートを処理した後、ユーザーのプロフィール画像のURLを更新します。
                    You can either update your local cache the next time you request the user’s information,
                    or, at least 5 seconds after uploading the image, ask for the updated URL using GET users / show.
                en: Updates the authenticating user’s profile image. Note that this method expects raw multipart data, not a URL to an image.
                    This method asynchronously processes the uploaded file before updating the user’s profile image URL.
                    You can either update your local cache the next time you request the user’s information,
                    or, at least 5 seconds after uploading the image, ask for the updated URL using GET users / show.
            * rate-limit:  times /  min
            * allowed parameter
                * image(MUST): gif, jpg, png
                * include_entities(optional):
                * skip_status:
            """
            path = 'account/update_profile'
            endpoint = Utils.create_endpoint('account/update_profile_image')


if __name__ == "__main__":
    api = Account(
        consumer_key=os.environ['TW_CONSUMER_KEY'],
        consumer_secret=os.environ['TW_CONSUMER_SECRET'],
        access_token=os.environ['TW_ACCESS_TOKEN'],
        access_secret=os.environ['TW_ACCESS_SECRET'],
    )
