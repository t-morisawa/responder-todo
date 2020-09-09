
# reponder-todo

 - TODOリスト
 - Responder(Python)
 - MySQL
 - Docker

# responderとは

https://responder.kennethreitz.org/en/latest/

# Dockerとは

https://docs.docker.jp/ 辺り?

# 起動までの手順

## Docker Composeを使う
```
docker-compose up --build
```

http://0.0.0.0 や http://localhost にアクセス

# デプロイ

## コンテナレジストリへpush
```
docker build -t responder-todo:lasest .
docker tag top:latest {レジストリのURI}:latest
docker push {レジストリのURI}:latest
```

### ECR(AWS)
```
aws ecr get-login-password --region ap-northeast-1 --profile {profile} | docker login --username AWS --password-stdin https://{アカウント名}.dkr.ecr.ap-northeast-1.amazonaws.com
docker tag responder-todo {アカウント名}.dkr.ecr.ap-northeast-1.amazonaws.com/responder-todo
docker push {アカウント名}.dkr.ecr.ap-northeast-1.amazonaws.com/responder-todo
```

### GCR(GCP)
```
docker tag responder-todo gcr.io/{PROJECT-ID}/responder-todo
docker push gcr.io/[PROJECT-ID]/responder-todo
```
