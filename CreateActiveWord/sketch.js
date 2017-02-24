var font;
var words = [];

function preload() {
    font = loadFont('libraries/THE_Oegyeinseolmyeongseo.ttf');
}

function setup() {
    var cnv = createCanvas(600,300);
    cnv.parent('main');
    var points = font.textToPoints('JinHan',30,200,192);
    console.log(points);

    for (var i = 0; i < points.length; i ++) {
        var pt = points[i];
        var word = new Word(pt.x,pt.y);
        words.push(word);
    }

}

function draw() {
    background(51);
    for (var i = 0; i < words.length; i ++) {
        var w = words[i];
        w.update();
        w.show();
    }
}
