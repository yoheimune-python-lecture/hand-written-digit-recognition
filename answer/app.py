from os import path
from sklearn.externals import joblib
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

    # 学習結果を読み込む.
    pklfile = path.join("result", "svm.pkl")
    clf = joblib.load(pklfile)

    # 予測する.
    predict = clf.predict([data])
    print("predict:", predict)

    return str(predict.tolist()[0])

if __name__ == "__main__":
    app.run(debug=True, port=5001)
