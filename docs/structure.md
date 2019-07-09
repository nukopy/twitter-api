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
