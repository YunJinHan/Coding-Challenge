var font;
var first = true;
var words;
var create = document.getElementById("button");

function preload() {
    font = loadFont('libraries/THE_Oegyeinseolmyeongseo.ttf');
    create.onclick = setup;
}

function setup() {
    words = [];
    var inputText = document.getElementById("input");
    var text = inputText.value;
    if (inputText.value == "" || inputText.value== null || typeof inputText.value == undefined) {
        text = "JinHan";
    }
    inputText.value = "";
    if (first === true) {
        var cnv = createCanvas(600,300);
        cnv.parent('main');
    }
    var points = font.textToPoints(text,20,200,192);
    var maxX = 0;
    for (var i = 0; i < points.length; i ++) {
        var pt = points[i];
        var word = new Word(pt.x,pt.y);
        if (pt.x > maxX) {
            maxX = pt.x;
        }
        words.push(word);
    }
    if (first === false) {
        var canvasWidth = pt.x + 80;
        var cnv = createCanvas(canvasWidth,300);
        cnv.parent('main');
    }
    first = false;
}

function draw() {
    background(51);
    for (var i = 0; i < words.length; i ++) {
        var w = words[i];
        w.behaviors();
        w.update();
        w.show();
    }
}
