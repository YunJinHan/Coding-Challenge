var s;
var scl = 20;
var apple;
var state = document.getElementById("state");
var highscore = 0;
var restart;

function setup() {
    var cnv = createCanvas(500,500);
    cnv.parent("main");
    s = new Snake();
    restart == false;
    frameRate(20);
    pickLocation();
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
    var score = s.eat(apple,highscore);
    if (score > -1) {
        pickLocation();
        highscore = score;
    }
    restart = s.gameOver();
    if (restart) {
        state.innerText = "Game Start";
        restart == false;
    }
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
