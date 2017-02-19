var s;
var scl = 20;
var apple;

function setup() {
    var cnv = createCanvas(600,600);
    cnv.parent("main");
    s = new Snake();
    frameRate(10);
    pickLocation();
    var state = document.getElementById("state");
    state.innerText = "Game Start";
}

function pickLocation() {
    var cols = floor(width/scl);
    var rows = floor(height/scl);
    apple = createVector(floor(random(cols)), floor(random(rows)));
    apple.mult(scl);
}

function draw() {
    background(51);
    if (s.eat(apple)) {
        pickLocation();
    }
    s.gameOver();
    s.update();
    s.show();
    fill(255,0,100);
    rect(apple.x, apple.y, scl, scl);
}

function keyPressed() {
    if (keyCode == UP_ARROW) {
        s.dir(0,-1);
    } else if (keyCode == DOWN_ARROW) {
        s.dir(0,1);
    } else if (keyCode == RIGHT_ARROW) {
        s.dir(1,0);
    } else if (keyCode == LEFT_ARROW) {
        s.dir(-1,0);
    }
}
