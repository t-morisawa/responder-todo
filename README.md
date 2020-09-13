
# reponder-todo

 - TODOリスト
 - Responder(Python)
   - https://responder.kennethreitz.org/en/latest/
 - Tortoise
   - https://tortoise-orm.readthedocs.io/en/latest/
 - MySQL
 - Docker
 - GCP (Cloud Run, Cloud SQL)

# 起動までの手順

## Docker Composeを使う
```
docker-compose up --build
```

http://0.0.0.0 や http://localhost にアクセス

# デプロイ

## Cloud SQL
 - コンソールからMySQLサーバを作成・起動する
 - Cloud Shellなどから `mysql/init/create_db.sql` に記載のコマンドを実行してDB/テーブルを作成する
   - DBはコンソールからも作成可能

## push(GCR)
```
docker build -t responder-todo .
docker tag responder-todo gcr.io/{PROJECT-ID}/responder-todo
docker push gcr.io/[PROJECT-ID]/responder-todo
```

## Cloud Run
 - コンソールからサービスを作成して実行
 - 環境変数 `ENV` `PROJECT_NAME` を正しく設定
 - ポート `80`
 - 「Cloud SQL 接続」で作成したCloud SQLを指定

# 環境変数

 - `ENV`: `local` `prod`
 - `PROJECT_NAME`: GCPのPROJECT_NAME
