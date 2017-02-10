"""
    SVM適用前のデータの前処理を行います.
    MNISTファイル(gzip)を、CSVファイルに変換します.
"""
import os
import gzip
import struct

def csv_image(fname, type_):
    """
        画像データを出力します.
        @param {String} fname - MNISTのファイル名
        @param {String} type_ - one of { training | test }
    """
    print("%s processing..." % fname)

    # 画像データをGzipファイルから読み取ります.
    with gzip.open(os.path.join("mnist", fname), "rb") as f:
        _, cnt, rows, cols = struct.unpack(">IIII", f.read(16))
        # 画像読み込み
        images = []
        for i in range(cnt):
            binarys = f.read(rows * cols)
            images.append(",".join([str(b) for b in binarys]))

    # CSV結果として出力します.
    with open(os.path.join("csv", type_ + "_image.csv"), "w") as f:
        f.write("\n".join(images))


def csv_label(fname, type_):
    """
        ラベルデータを出力します.
        @param {String} fname - MNISTのファイル名
        @param {String} type_ - one of { training | test }
    """
    print("%s processing..." % fname)

    # ラベルデータをGzipファイルから読み取ります.
    with gzip.open(os.path.join("mnist", fname), "rb") as f:
        _, cnt = struct.unpack(">II", f.read(8))
        labels = []
        for i in range(cnt):
            label = str(struct.unpack("B", f.read(1))[0])
            labels.append(label)

    # CSV結果として出力します.
    with open(os.path.join("csv", type_ + "_label.csv"), "w") as f:
        f.write("\n".join(labels))


if __name__ == "__main__":

    if not os.path.exists("csv"):
        os.mkdir("csv")

    # トレーニングデータ.
    csv_image("train-images-idx3-ubyte.gz", "training")
    csv_label("train-labels-idx1-ubyte.gz", "training")

    # テストデータ.
    csv_image("t10k-images-idx3-ubyte.gz", "test")
    csv_label("t10k-labels-idx1-ubyte.gz", "test")
