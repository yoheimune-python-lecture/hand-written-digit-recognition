from os import path
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    """HTMLページをレンダリングします."""
    return render_template("index.html")

@app.route("/api/judge")
def api_judge():
    """手書き文字を判定します"""

    # クライアントからのデータを受け取る.
    data = request.args.get("data").split(",")
    data = [int(d) / 256 for d in data]
    print(data)


    """
        **** ここを実装します（基礎課題） ****
        学習済みのモデル（SVM）を読み込み、手書き文字が何の数値なのかを判定します。
        判定結果をAPIで返すことでフロントエンドに伝えます。

        実装ステップ：
            ・学習結果（`result/svm.pkl`）を読み込む
            ・クライアントから渡ってきたデータをもとに、予測を行う
            ・予測結果を返す

        参考になる情報
            講義スライドや答えを適宜確認しながら実装してみてください。

        ここが演習の最後です。
        頑張ってください！
    """

    # ダミー
    return "-1"

if __name__ == "__main__":
    app.run(debug=True, port=5002)
