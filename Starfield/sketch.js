var star = [];
var speed;
var state = document.getElementById("state");

function setup() {
    var cnv = createCanvas(600,600);
    cnv.parent("main");
    state.innerText = "Mouse Left Move : Star Stop\nMouse Right Move : Star Move";
    for (var i = 0; i < 500; i ++) {
        star[i] = new Star();
    }
}

function draw() {
    background(0);
    translate(width/2,height/2);
}
