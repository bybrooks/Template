### dockerコマンドがユーザー権限で利用できない場合
```
sudo chown <user_name> /var/run/docker.sock
```

### 使っていないイメージをクリーンアップ
```
docker image prune
```