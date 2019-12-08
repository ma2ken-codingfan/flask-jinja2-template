from flask import *  # 必要なライブラリのインポート

app = Flask(__name__)  # アプリの設定


@app.route("/", methods=["GET", "POST"])  # どのページで実行する関数か設定
def main_page():
    return render_template("mainpage.html")


@app.route("/<name>", methods=["GET", "POST"])
def namepage(name):
    return render_template("name.html", name=name)

if __name__ == "__main__":  # 実行されたら
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)  # デバッグモード、localhost:8888 で スレッドオンで実行
