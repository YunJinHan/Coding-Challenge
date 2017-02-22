var star = [];
var speed;
var state = document.getElementById("state");

function setup() {
    var cnv = createCanvas(600,600);
    cnv.parent("main");
    state.innerText = "Mouse UP Move : Star Move Slow\nMouse DOWN Move : Star Move Fast";
    for (var i = 0; i < 500; i ++) {
        star[i] = new Star();
    }
}

function draw() {
    speed = map(mouseY, 0, height, 1, 20);
    background(0);
    translate(width/2,height/2);
    for (var i = 0; i < star.length; i ++) {
        star[i].update();
        star[i].show();
    }
}
