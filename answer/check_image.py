"""
    CSV出力した画像データが正しいか否かを判断するために、
    一部を画像データとして出力してみます.
"""
import os

CNT = 100

if __name__ == "__main__":

    if not os.path.exists("image"):
        os.mkdir("image")

    with open(os.path.join("csv", "training_image.csv")) as f:
        images = f.read().split("\n")

    for i, image in enumerate(images[:CNT]):
        with open(os.path.join("image", "%d.pgm" % i), "w") as fw:
            s = "P2 28 28 255\n"
            s += " ".join(image.split(","))
            fw.write(s)
