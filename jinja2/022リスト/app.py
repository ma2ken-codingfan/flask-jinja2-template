from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    title = 'リストを渡す'
    main_title = '022リスト'
    shikoku_list = ['愛媛県', '高知県', '徳島県', '香川県']
    return render_template('index.html', shikoku=shikoku_list, title=title, main_title=main_title)


if __name__ == "__main__":  # 実行されたらpip
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)
