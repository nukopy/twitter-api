# Python Library for Twitter REST Public API

## どういう設計にするのか

- API
- 各ひとかたまりのデータのためのデータモデルクラス．(User とか)
- ページネーションのための API のヘルパークラス
- エラーオブジェクト（エラーや API リミットなど）
- ロガー
- utils(utility の複数形，便利関数クラス)，URL パーサとか

## twitter-api の設計

### ディレクトリ構造

tree の実行結果

```bash
tree twitter-api

twitter-api
├── LICENSE
├── MANIFEST.in
├── Makefile
├── README.rst
├── docs
│   ├── Makefile
│   ├── conf.py
│   ├── doc.md
│   ├── index.rst
│   ├── make.bat
│   └── structure.md
├── requirements.txt
├── response_samples
│   └── account
│       ├── GET_settings.json
│       ├── GET_verify_credentials.json
│       ├── POST_settings.json
│       ├── POST_update_profile_background_image.json
│       └── POST_update_profile_image.json
├── setup.py
├── tests
│   ├── __init__.py
│   ├── context.py
│   ├── test_advanced.py
│   └── test_basic.py
└── twitter（アプリ部分）
    ├── __init__.py
    ├── api.py
    ├── core.py
    ├── endpoints
    │   ├── account.py
    │   ├── application.py
    │   ├── blocks.py
    │   ├── direct_messages.py
    │   ├── favorites.py
    │   ├── followers.py
    │   ├── friends.py
    │   ├── friendships.py
    │   ├── geo.py
    │   ├── help.py
    │   ├── lists.py
    │   ├── media.py
    │   ├── mutes.py
    │   ├── saved_searches.py
    │   ├── search.py
    │   ├── statuses.py
    │   ├── trends.py
    │   ├── twitter
    │   │   ├── api.py
    │   │   └── utils.py
    │   └── users.py
    ├── filter_none.png
    ├── helpers.py
    ├── models.py
    ├── pycallgraph_example.py
    ├── test_tweepy.png
    ├── test_tweepy.py
    └── utils.py
```

### 設計

- できる限り API（というより，エンドポイント）に沿ったライブラリにしたい．
- まずは API 通りに実行できるクラスを作成し，その後に簡単なタイムラインの取得，ユーザ情報の取得などをそれらをラップして作成する．
- twitter/endpoints では原則レスポンスを返すのみにする．それらをラップして JSON をうまく整形する方法を考える．（`data.screen_name` みたいにプロパティとしてアクセスできるようになったら嬉しい）．

* ラッパーというよりはレスポンスを上手く返してくれる（ヘッダ情報などを含めた）

### データの振り分け

大きく分けて，

- レスポンスヘッダ（メタデータ）
- レスポンスボディ（エンドポイントごとの使いたいデータ）

一つのエンドポイントを呼ぶごとに，

- ヘッダでメタ情報の読み込み．
- rate_limit_status を読みに行く（これはヘッダで十分か？）．
- ロガーを噛ませる

そして，必要なデータを属性として呼べるようにしたい．例えば，以下のような感じで（**これは setattr で実現できるのではないか？**）．

```python
user.screen_name
user.id
```

### 各レスポンスについて共通するデータを抜き出してモデル化

- レスポンスの中に共通するデータが存在する．
- entities, status など．
- **entities, status を含めると大きく構造が変わるが，それはどうするのか？内容は同じなので，それ専用の関数などを作る（`if include_entities == True` みたいな）**
- これも自動で読み取って構造化してくれるようにしたい．
- 最終的に JSON レスポンスをアトリビュートで全てアクセスできるようにしたい．

## HTTP レスポンスの構造

### requests.models.Response オブジェクトの属性（プロパティ，アトリビュート）

- [Official Doc](https://2.python-requests.org/en/master/api/)

#### 使う属性

- requests.models.Response
  - apparent_encoding：見かけのエンコーディング（即時推定する）
  - headers: requests.structures.CaseInsensitiveDict（requests 専用の大文字，小文字を問わない辞書型）
  - json(): dict
  - ok: boolean
  - raise_for_status(): None or requests.HTTPError
  - reason: str
  - status_code: int
  - text: str
  - url: str

#### 使う属性に関する説明

- requests.models.Response

  - apparent_encoding：見かけのエンコーディング（即時推定する）
  - headers：HTTP ヘッダ
  - json(): レスポンスボディを辞書型で返す．レスポンスの中身本体を表す．もしレスポンスボディが JSON を含まない場合（HTML など），ValueError が呼ばれる．
  - ok: `status_code` が 400 未満であれば True（成功 or リダイレクト）．
  - raise_for_status(): エラーが起きた場合，`requests.HTTPError` を格納する．(**使わない**)
  - reason: HTTP ステータスを文字列で返す（"OK", "Forbidden", "Not Found"）．
  - status_code：ステータスコードを int 型で返す（404, 200）．
  - text: リクエスト先の HTML，JSON レスポンスを文字列として返す．このとき，エンコーディングは `res.encoding` の値が使われる（これ自体は HTTP ヘッダに基づいて決められる）．もしエンコーティングを自分で指定したい場合，`res.text` を実行する前に，`res.encoding = 'utf-8'` などを実行して `res.text` を実行すれば，自分の好きなエンコーディングでレスポンスボティを得ることができる．
  - url：リクエスト先の URL

#### 使わない属性

- requests.models.Response

  - c
  - close()：コネクションを閉じる？raw オブジェクトが存在するとき以外使わない方が良い？
  - connection
  - content：HTTP レスポンスを bytes 型で返す
  - cookies：Web サーバが，Web ブラウザを通じて訪問者のコンピュータに一時的にデータを書き込んで保存させる仕組み．HTTP レスポンスに含まれる．

  - e
  - elapsed：レスポンス送ってから帰ってくるまでの時間？between sending the request and the arrival of the response
  - encoding：実際に使われているエンコーディング（apparent の方は実行されるたびに body を読み取って推定したエンコーディングを返してくれる）．これを設定するとエンコーディングの設定を変えることができる．

  - h
  - history：リダイレクトが起こった時の記録．

  - i
  - is_permanent_redirect：301 リダイレクト．URL が恒久的に変更された場合に用いられる転送処理のステータスコード．そのフラグ．
  - is_redirect：302 リダイレクト．URL が一時的な転送を表すもの．そのフラグ．
  - (bytes)iter_content(chunk_size=1, decode_unicode=False)：stream オプションが True のときに，大きなレスポンスデータが一度にメモリ上に乗らないようにする．小分け（chunk size: データの読み書きの単位．引数には bytes を入れる）にして繰り返し読み込ませる必要がある．If decode_unicode is True, content will be decoded using the best available encoding based on the response.
    デコードユニコードが True のとき，コンテンツは bytes 型からベストなエンコーディングにデコードされる．
  - (bytes)iter_lines(chunk_size=512): iter_content はチャンクサイズが小さいが，lines は 1 行を単位とする．

  - l, n
  - links：HTTP レスポンスヘッダ内の Link: ヘッダをパースしたものを提供する．`res.headers` でアクセスすると文字列としてしか得られないが，`res.links` とすると，各リンクがちゃんとパースされた状態で得られる．
  - next：リダイレクトのための次のリクエスとオブジェクトを返す．リダイレクトがない場合は None．

  - r
  - request: `PreparedRequest` オブジェクトを返す．セッションで送信することができる状態（HTTP リクエストで送ったものをそのままセッションに渡して再現できる）．
  - raw: 生データ？

## 疑問点

- `PreparedRequest` とは？

## 補足

### チャンクサイズ chunk size

- データの読み書きを行う単位のこと．
- イテレーションは，配列やそれに類似するデータ構造の各要素に対する繰り返し処理の抽象化．メモリに乗り切らない大きなデータを少しずつメモリに乗せて順次読み取ることなどに利用できる．

### HTTP Link Header

- HTTP レスポンスで他の関連リソースへのリンクを提供．

- リンク（Link:）HTTP ヘッダは，クライアントにリクエストされたリソースについてのメタデータを含む，異なるリソースを知らせる（要はリクエストされたリソースに関する他の情報を Link ヘッダによって提供する）．

Link ヘッダによって，異なる関連リソースのリンクを送信してリソースの他の情報を提供することができる．例えば，

- A map of different language, content-type and version-specific URIs
- Licensing, such as Creative Commons
- Information about how to edit the file
- Policy information about appropriate use and/or distribution of the data

- The HTTP Link entity-header field provides a means for **serialising one or more links in HTTP headers**. It is semantically equivalent to the HTML `<link>` element.
