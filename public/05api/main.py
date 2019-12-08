from flask import *

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


@app.route("/")
def index():
    return jsonify({"language": "パイソンパイソン"}), 418


if __name__ == "__main__":  # 実行されたら
    app.run(host='0.0.0.0', port=8888)
