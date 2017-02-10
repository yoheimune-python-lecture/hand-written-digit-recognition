"use strict";

/**
 * 描画中か否かを判定するフラグ.
 */
let drawing = false;

/**
 * 描画するマウスの軌跡を保持する変数.
 */
let points = [];

/**
 * Canvas要素.
 */
let canvas;

/**
 * Canvasのコンテキスト要素.
 */
let context;

/**
 * サーバー通信を行う.
 */
function api(url) {
    return new Promise((resolve, reject) => {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', url, true);
        xhr.onreadystatechange = function (e) {
            if (this.readyState === 4 && this.status === 200) {
                resolve(this.responseText);
            }
        }
        xhr.send();
    });
}

/**
 * Canvasに手書き文字を描画します.
 */
function draw() {

    context.clearRect(0, 0, canvas.width, canvas.height);
    context.lineWidth = 40;
    context.lineCap = 'round';

    for (let i = 0; i < points.length; i++) {
        let p1 = points[i];
        let p2 = points[i + 1];
        if (p1 && p2) {
            context.beginPath();
            context.moveTo(p1.x, p1.y);
            context.lineTo(p2.x, p2.y);
            context.stroke();
        }
    }
}

/**
 * 手書き文字の判定を行います.
 */
function judge() {

    // 28 x 28 に圧縮する.
    let img = new Image();
    img.src = canvas.toDataURL();
    img.onload = () => { 

        let tmpCanvas = document.createElement('canvas');
        tmpCanvas.width = 28;
        tmpCanvas.height = 28;
        tmpCanvas.getContext('2d').drawImage(img, 0, 0, 28, 28);

        let imgResize = new Image();
        imgResize.src = tmpCanvas.toDataURL();
        imgResize.onload = () => {


            // 28 x 28 からピクセル要素を抜き出します.
            let data = [];
            var imgd = tmpCanvas.getContext('2d').getImageData(0, 0, 28, 28);
            var pixcels = imgd.data;
            for (let i = 0; i < pixcels.length; i += 4) {
                let alpha = pixcels[i + 3];
                console.log(pixcels[i + 0], pixcels[i + 1], pixcels[i + 2], pixcels[i + 3]);
                data.push(alpha);
            }

            // 何も描画されていなかったら、判定しない.
            let tmp = data.filter(d => d > 0);
            if (tmp.length === 0) {
                return;
            }

            // サーバーで判定を行い、結果を表示する.
            let url = '/api/judge?data=' + data.join(',');
            api(url).then(result => {
                document.getElementById('result').innerHTML = result;
            });
        }
    }
}

/**
 * マウスダウンのイベントを扱います.
 */
function handleMouseDown(e) {
    drawing = true;
    points = [];
}

/**
 * マウス移動のイベントを扱います.
 */
function handleMouseMove(e) {

    if (drawing) {
        let rect = canvas.getBoundingClientRect();
        let x = Math.max(0, e.clientX - rect.left);
        let y = Math.max(0, e.clientY - rect.top);
        points.push({x, y});
        draw();
    }
}

/**
 * マウスアップのイベントを扱います.
 */
function handleMouseUp() {
    draw();
    drawing = false;
    judge();
}

/**
 * マウスリーヴのイベントを扱います.
 */
function handleMouseLeave() {
    drawing = false;
}

/**
 * 削除ボタンへのクリックを扱います.
 */
function handleDelButtonClick() {
    points = [];
    draw();
}

// アプリケーションを開始します.
window.addEventListener('DOMContentLoaded', () => {

    canvas = document.getElementById('canvas');
    context = canvas.getContext('2d');

    canvas.onmousedown = handleMouseDown;
    canvas.onmousemove = handleMouseMove;
    canvas.onmouseup = handleMouseUp;
    canvas.onmouseleave = handleMouseLeave;

    document.getElementById('delButton').onclick = handleDelButtonClick;
});