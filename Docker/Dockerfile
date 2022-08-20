FROM *** 

# WIP
LABEL

# RUNはイメージ作成時に指定したコマンドが実行される
# pip install等はRUNで実施
# CMDでやっても反映されない
RUN apt-get update && apt-get install -y \
    package1 \
    package2 
    
# CMDはコンテナ開始時 or 作成時(docker start or docker run)に指定したコマンドが実行される
CMD ["excutable", "param1", "param2"]

# コンテナ側で露出するポート番号
# docker run -p 5000:80 (host:container)
EXPOSE 80

# コンテナ内で使用する環境変数設定
# 環境変数を参照するときは$PACKAGE_VERSIONとドルマークを付けて使用する
ENV PACKAGE_VERSION=3.2.3

# local files(dirも？)をcontainer側にcopyする
# ADDはCOPY以上の機能があるため、コピーに留まる要件であればCOPYが推奨される
COPY "local側のpath" "container側のpath"