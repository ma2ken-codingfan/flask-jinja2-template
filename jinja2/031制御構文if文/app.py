from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    title = '031制御文 if文'
    main_title = '031制御文 if文'
    return render_template('index.html', num=1, title=title, main_title=main_title)


if __name__ == "__main__":  # 実行されたらpip
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)
