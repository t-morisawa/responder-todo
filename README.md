
# reponder-todo

 - TODOリスト
aaaa
test

# responderとは

https://responder.kennethreitz.org/en/latest/

# Dockerとは

https://docs.docker.jp/ 辺り?

# 起動までの手順

## Docker Composeを使う
```
docker-compose up --build
```

## [depricated] Docker Composeを使わず、単独でコンテナを立ち上げる

```
docker build -t responder-todo .
docker run -it -p 80:80 responder-todo
```

http://0.0.0.0 や http://localhost にアクセス
