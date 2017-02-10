"""
    MNISTファイルをダウンロードして、`mnist/`以下に保存します.
"""
import os
from urllib.request import urlopen

def download(fname):
    """指定されたMNISTファイルをサーバーから取得します"""
    print("%s downloading..." % fname)
    with urlopen("http://yann.lecun.com/exdb/mnist/" + fname) as res:
        d = res.read()
        with open("mnist/" + fname, "wb") as f:
            f.write(d)

if __name__ == "__main__":

    if not os.path.exists("mnist"):
        os.mkdir("mnist")

    download("train-images-idx3-ubyte.gz")
    download("train-labels-idx1-ubyte.gz")
    download("t10k-images-idx3-ubyte.gz")
    download("t10k-labels-idx1-ubyte.gz")
