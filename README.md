# 手書き文字を判定しよう
これはPython講義のデモアプリの1つで、 Pythonで機械学習を行う練習課題です.  
手書きで0〜9のいずれかの数値を書くと、それが何なのかを判定して画面に表示します.
***
![手書き文字を判定しよう](https://raw.githubusercontent.com/yoheimune-python-lecture/hand-written-digit-recognition/image/resources/screenshot.png)
[デモはこちら](http://demo-digit-recognition.paint-ink.com/)  

# 演習の準備
以下の手順で演習を進めることができます。
## レポジトリの取得
以下の要領で、レポジトリを取得してローカルにソースコードを持ってきます.
```
# リポジトリをクローン.
git clone https://github.com/yoheimune-python-lecture/hand-written-digit-recognition.git
```
ローカルへクローン（=ダウンロード)したら、 `hand-written-digit-recognition` フォルダができるので、移動しておきます。
```
# ダウンロードしたフォルダへ移動.
cd hand-written-digit-recognition
```
## 必要ライブラリのインストール
利用するライブラリを `pip`でインストールします.
```
pip3 install --upgrade flask
pip3 install --upgrade numpy
pip3 install --upgrade matplotlib
pip3 install --upgrade scipy
pip3 install --upgrade scikit-learn
```
## 起動確認
まずは起動してみて動くことを確認します.
```
cd practice
python3 app.py
```
以下のURLでアクセス可能です。
```
http://localhost:5002
```

# 基礎課題
この演習では、Pythonで機械学習を行う実装を行います。修正するプログラムは以下です。  
- prepare.py：MNISTのデータからCSVを出力します.  
- svm.py：SVMを用いた機械学習を行います.  
- app.py：学習済みの結果を用いて、手書きの数値文字を判定します.  

それぞれの該当ファイルに具体的な演習内容を記述しています。  
無事に動くことを祈っています！！！  

# 発展課題
上記が完成しましたら、学習サンプル数を変更してみたり、他のアルゴリズムを試したりとぜひ遊んでみてください。

# 課題の答え
課題の答えは、以下にありますので、適宜ご確認ください。  

[課題の答えはこちら](https://github.com/yoheimune-python-lecture/hand-written-digit-recognition-answer)  
