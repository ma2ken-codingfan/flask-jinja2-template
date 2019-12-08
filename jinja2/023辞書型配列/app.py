from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    title = 'リストを渡す'
    main_title = '023辞書型配列'
    fruit_dict = {'orange': 100, 'apple': 200}
    return render_template('index.html', fruit=fruit_dict, title=title, main_title=main_title)


if __name__ == "__main__":  # 実行されたらpip
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)
