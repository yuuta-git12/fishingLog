#!/bin/sh

# オプション --noinput：非対話モードで実行
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
# 環境変数のDEBUGの値がTrueの時はrunserverを、Falseの時はgunicornを実行します
# シェルスクリプトでは`[`と`$DEBUG`、`1`と`]`の間にスペースを一つ空けておかないと[]内の式を認識できないので注意
if [ $DEBUG = 1 ]; then
    python manage.py runserver 0.0.0.0:8000
else
    # gunicornを起動させる時はプロジェクト名を指定します
    # 今回はdjangopjにします
    gunicorn fishing_log.wsgi:application --bind 0.0.0.0:8000
fi
