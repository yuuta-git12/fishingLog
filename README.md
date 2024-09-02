# Djangoで作成する自作アプリ
## 説明
- PythonフレームワークのDjangoの開発環境
- 開発環境はdockerコンテナを使用

## ディレクトリ構成
```
.
├── .env：開発用の環境変数の設定ファイル
├── .env.prod：本番用の環境変数の設定ファイル
├── .gitignore
├── READEME.md
├── containers
│   ├── django
│   │   ├── Dockerfile：DjangoのDockerfile
│   │   └── entrypoint.sh：Djangoのコマンドを実行する為のシェルスクリプト
│   ├── nginx
│   │   ├── Dockerfile：nginxのDockerfile
│   │   └── conf.d
│   │       └── default.conf：nginx用の設定ファイル
│   └── postgres
│       └── Dockerfile：postgreSQLのDockerfile
├── docker
├── docker-compose.prod.yml：本番用のymlファイル
├── docker-compose.yml：開発用のymlファイル
└── requipments.ext
```
## 開発環境の構成


## コンテナの起動・停止
### Docker imageの作成(初回)
- プロジェクトを新規作成する際、プロジェクト名と作成するディレクトリを指定して以下のコマンドを実行
```
docker compose -f <指定するdokcer-composeのファイル> run app django-admin startproject <プロジェクト名> <プロジェクトを作成するディレクトリ>

例：docker compose -f docker-compose.yml run app django-admin startproject djangopj .

```
### すでにプロジェクトがある場合
```
docker compose -f <指定するdokcer-composeのファイル> build
```

### settings.pyのDATABASESを変更
- memo_settings.mdの内容を参考に/<プロジェクト名>/settings.pyの内容を変更

### 開発環境の場合
- 起動
  `docker compose -f docker-compose.yml up -d`
- 停止
  `docker stop fish_log`
  `docker stop postgres`
  

### 運用環境の場合
  `docker compose -f docker-compose.prod.yml up -d    `



## 参考サイト
- [Docker+Django+Nginx+PostgreSQL+Gunicornで環境構築~M1Mac対応](https://qiita.com/shun198/items/ee93c50eac2f7c77e443)