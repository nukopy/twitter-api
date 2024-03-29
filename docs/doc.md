# Twitter REST API: Public API

- メディアをアップロードする
- 検索用 API
- 検索用 API: 場所ごとのツイート
- タイムラインを処理する
- API レート制限
- API レート制限: 早見表

## 代表的なエンドポイント

Twitter で使える機能ごとにエンドポイントが別れている．

- account
- application
- blocks
- direct_messages
- favorites
- followers
- friends（フォロー）
- friendships
- geo
- help
- lists（今回使うやつ）
- media
- mutes
- users
- saved_searches
- search
- statuses
- trends

## account

アカウント設定のデータを取り扱うエンドポイント．

- GET account/settings 認証ユーザーのアカウント設定を取得する。
- GET account/verify_credentials 認証ユーザーのアカウントが有効な状態か確認する。
- POST account/remove_profile_banner バナー画像を削除する。
- POST account/settings アカウントの設定を更新する。
- POST account/update_profile プロフィールを更新する。
- POST account/update_profile_background_image プロフィールの背景画像を更新する。
- POST account/update_profile_banner プロフィールのバナー画像を更新する。
- POST account/update_profile_image プロフィールのアイコン画像を更新する。

## application

レートリミットの情報を取り扱うエンドポイント．

- GET application/rate_limit_status レートリミット設定と使用状況を取得する。

## blocks

ブロック関係のデータを取り扱うエンドポイント．

- GET blocks/ids ブロックしているユーザーを、ユーザー ID で取得する。
- GET blocks/list ブロックしているユーザーを、ユーザーオブジェクトで取得する。
- POST blocks/create ブロックを実行する。
- POST blocks/destroy ブロックを解除する。

## direct_messages

ダイレクトメッセージのデータを取り扱うエンドポイント．

- GET direct_messages 受信したダイレクトメッセージを取得する。
- GET direct_messages/sent 送信したダイレクトメッセージを取得する。
- GET direct_messages/show 個別のダイレクトメッセージの内容を取得する。
- POST direct_messages/destroy ダイレクトメッセージを削除する。
- POST direct_messages/new ダイレクトメッセージを送信する。

## favorites

お気に入り関係のデータを取り扱うエンドポイント．

- GET favorites/list 対象ユーザーがお気に入りに登録したツイートの一覧を取得する。
- POST favorites/create 対象ツイートにいいねを付ける。
- POST favorites/destroy 対象ツイートのいいねを取り消す。

## followers

フォロワー関係のデータを取り扱うエンドポイント．

- GET followers/ids 対象ユーザーのフォロワーを、ID の一覧で取得する。
- GET followers/list 対象ユーザーのフォロワーを、オブジェクトの一覧で取得する。

## friends（フォロー）

フォロー関係のデータを取り扱うエンドポイント．

- GET friends/ids 対象ユーザーがフォローしているユーザーを、ID の一覧で取得する。
- GET friends/list 対象ユーザーがフォローしているユーザーを、オブジェクトの一覧で取得する。

## friendships

ユーザー間の関係に関するデータを取り扱うエンドポイント．

- GET friendships/incoming 自分に対してフォローリクエストを送っているユーザーを取得する。
- GET friendships/lookup 自分と対象ユーザーとの関係を取得する。
- GET friendships/no_retweets/ids 自分が RT 非表示中のユーザーを取得する。
- GET friendships/outgoing 自分がフォローリクエストを送っているユーザーを取得する。
- GET friendships/show 2 人のユーザーの関係を取得する。
- POST friendships/create フォローする。
- POST friendships/destroy フォローを解除する。
- POST friendships/update リツイート非表示、ツイート通知の設定を更新する。

## geo

場所や位置座標の情報を取り扱うエンドポイント．

- GET geo/id/:place_id 場所の情報を取得する。
- GET geo/reverse_geocode 緯度、経度から場所の情報を取得する。
- GET geo/search 場所を検索する。

## help

Twitter のルール関係のデータを取り扱うエンドポイント．

- GET help/configuration Twitter の内部設定を取得する。
- GET help/languages Twitter が対応している言語の一覧を取得する。
- GET help/privacy Twitter のプライバシーポリシーを取得する。
- GET help/tos Twitter のサービス利用規約を取得する。

## lists（今回使うやつ）

リスト関係のデータを取り扱うエンドポイント．

- GET lists/list 対象ユーザーのリスト一覧を取得する。
- GET lists/members 対象のリストにメンバー(発言者)として加えられているユーザーの一覧を取得する。
- GET lists/members/show 対象のリストに、対象のユーザーがメンバーとして加わっているか否かを確認する。
- GET lists/memberships lists/members/memberships(GET メソッド)は、対象ユーザーが、メンバー(発言者)として加えられているリストの一覧を取得するエンドポイントです。
- GET lists/ownerships 対象ユーザーが作成したリストの一覧を取得する。
- GET lists/show 対象のリストを取得する。
- GET lists/statuses リストのタイムラインを取得する。
- GET lists/subscribers リストの購読者を取得する。
- GET lists/subscriptions ユーザーが購読しているリストを取得する。
- POST lists/create リストを作成する。
- POST lists/destroy リストを削除する。
- POST lists/members/create リストにメンバーを追加する。
- POST lists/members/create_all リストに複数のメンバーを追加する。
- POST lists/members/destroy リストからメンバーを削除する。
- POST lists/members/destroy_all リストから複数のメンバーを削除する。
- POST lists/subscribers/create リストを保存する。
- POST lists/subscribers/destroy リストの購読を取り消す。
- POST lists/update リストの設定を更新する。

## media

メディアアップロードをするエンドポイント．

- POST media/upload 画像をアップロードする。
- POST media/upload (APPEND) 動画のアップロードを実行する。
- POST media/upload (FINALIZE) 動画のアップロードを完了する。
- POST media/upload (INIT) 動画のアップロードを準備する。

## mutes

ミュート関係のデータを取り扱うエンドポイント．

- GET mutes/users/ids 自分がミュートしているユーザーを、ユーザー ID の一覧で取得する。
- GET mutes/users/list 自分がミュートしているユーザーを、オブジェクトの一覧で取得する。
- POST mutes/users/create ミュートを実行する。
- POST mutes/users/destroy ミュートを解除する

## saved_searches

検索メモ関係のデータを取り扱うエンドポイント．

- GET saved_searches/list 検索メモを一覧で取得する。
- GET saved_searches/show/:id 検索メモを個別に取得する。
- POST saved_searches/create 検索メモを保存する。
- POST saved_searches/destroy/:id 検索メモを削除する。

## search（重要）

ツイートの検索 API を利用できます。

- GET search/tweets ツイートを検索する。

## statuses（重要）

ツイート関係のデータを取り扱うエンドポイント．

- GET statuses/home_timeline ホームタイムラインを取得する。
- GET statuses/lookup ツイートを任意の数だけ取得する。
- GET statuses/mentions_timeline メンションタイムラインを取得する。
- GET statuses/oembed 対象ツイートの埋め込み用コードを取得する。
- GET statuses/retweeters/ids 対象ツイートをリツイートしたユーザーを、ユーザー ID の一覧で取得する。
- GET statuses/retweets/:id 対象ツイートをリツイートしたユーザーを、オブジェクトの一覧で取得する。
- GET statuses/retweets_of_me リツイートされたツイートの一覧を取得する。
- GET statuses/show/:id ツイートを個別に取得する。
- GET statuses/user_timeline ユーザータイムラインを取得する。
- POST statuses/destroy/:id ツイートを削除する。
- POST statuses/retweet/:id リツイートを実行する。
- POST statuses/unretweet/:id リツイートを取り消す。
- POST statuses/update ツイートを投稿する。

## trends

トレンドの情報を取り扱うエンドポイント．

- GET trends/available トレンドの集計対象となっている地域の一覧を取得する。
- GET trends/closest 位置座標から WOEID を取得する。
- GET trends/place トレンドワードを取得する。

## users（重要）

ユーザープロフィールに関係するデータを取り扱うエンドポイント．

- GET users/lookup 複数のユーザーの情報を取得する。
- GET users/profile_banner プロフィールのバナー画像を取得する。
- GET users/search ユーザーを検索する。
- GET users/show ユーザーのプロフィールを取得する。
- GET users/suggestions サジェストのカテゴリを取得する。
- GET users/suggestions/:slug おすすめユーザーを取得する。
- GET users/suggestions/:slug/members おすすめユーザーをツイート付きで取得する。
- POST users/report_spam スパム報告を実行する。
