## ユーザー回り
### 新規ユーザーを追加
```
sudo adduser [USER_NAME]
```
### ユーザーにsudo権限を付与する
```
sudo usermod -aG [USER_NAME]
```
### グループと所属ユーザーの一覧表示
```
cat /etc/group

# grepでsudo権限を持つユーザー確認
cat /etc/group | grep sudo
```

## ファイル権限回り
### ファイルの所有者を変更
```
chown [変更先のUSER_NAME] [FILE_NAME]

## 再帰的に変更
chown -R [変更先のUSER_NAME] [FILE_NAME]
```
