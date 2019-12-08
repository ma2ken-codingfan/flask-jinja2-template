# 楽天ブログ更新のため

## 参考リンク

[Flaskのjinja2テンプレートエンジンのチートシート](https://tanuhack.com/jinja2-cheetsheet/)

[はじめての Flask](https://qiita.com/nagataaaas/items/d249c3905d41137cd510)
[flask Document(英)](https://flask.palletsprojects.com/en/1.1.x/)
[flask Document(日)](https://flask.palletsprojects.com/en/1.1.x/)
[Python Flask 入門](python.zombie-hunting-club.com/entry/2017/11/03/223503)
[2. Flask チュートリアル](https://study-flask.readthedocs.io/ja/latest/02.html)

[flask wiki](https://ja.wikipedia.org/wiki/Flask)

## python 仮想コマンド venv

```shell
// 仮想環境構築
python -m venv venv

// 起動
. venv/Scripts/activate

// Flask install
pip install -U pip
pip install flask

// Flask 起動
python app.py // ディレクトリ配下でアプリ起動

// 終了
deactivate


pip install -U pip
pip install flask

// 再構築するためのファイル作成と再インストール
pip freeze > requirements.txt
pip install -r requirements.txt
```

## browser-sync

```shell
npm install -D browser-sync



npx browser-sync start --proxy '0.0.0.0:8888' --serveStatic 'public' --files 'public'
```
