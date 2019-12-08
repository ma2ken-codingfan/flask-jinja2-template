from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def input():
    return render_template('index.html', title='入力ページ')


# HTMLのformタグのmethod属性が指定したメソッドタイプを取得
@app.route('/', methods=['POST'])
def output():
    # HTMLのformタグで送信される<input type="hoge">のクエリパラメータを取得
    name = request.form['name']
    age = request.form['age']
    html = render_template('output.html', name=name,
                           age=age, title='出力ページ')  # 最後にHTMLファイルとして保存
    with open("templates/test.html", mode='w', encoding="utf-8", newline="\n") as f:
        f.write(str(html))

    return html


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)
