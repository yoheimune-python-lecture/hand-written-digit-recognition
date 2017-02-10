"""
    SVMアルゴリズムで手書き文字の判定を学習し、また結果を評価します.
"""
import os
from sklearn import svm, metrics
from sklearn.externals import joblib

# 学習用データの数
SIZE_TRAINING = 500

# 検証用データの数
SIZE_TEST = 500

def load_data(type_, size):
    """
        イメージとラベルのデータを取得して返却します.
        またここで学習しやすいように、各数値を256で割って1以下の数値にします.

        @param {String} type_ - one of { training | test }
        @param {Int} size - 返却する要素数
    """

    with open(os.path.join("csv", "%s_image.csv" % type_)) as f:
        images = f.read().split("\n")[:size]
    with open(os.path.join("csv", "%s_label.csv" % type_)) as f:
        labels = f.read().split("\n")[:size]

    images = [[int(i)/256 for i in image.split(",")] for image in images]
    labels = [int(l) for l in labels]

    return images, labels


if __name__ == "__main__":

    # トレーニングデータを取得します.
    images, labels = load_data("training", SIZE_TRAINING)

    # 学習
    print("学習開始")
    clf = svm.SVC()
    clf.fit(images, labels)

    # テストデータを取得します.
    images, labels = load_data("test", SIZE_TEST)

    # 予測
    print("予測開始")
    predict = clf.predict(images)

    # 結果表示
    print("結果だよー")
    ac_score = metrics.accuracy_score(labels, predict)
    cl_report = metrics.classification_report(labels, predict)
    print("正解率 = ", ac_score)
    print(cl_report)

    # 結果を保存する
    if not os.path.exists("result"):
        os.mkdir("result")
    joblib.dump(clf, os.path.join("result", "svm.pkl"))
