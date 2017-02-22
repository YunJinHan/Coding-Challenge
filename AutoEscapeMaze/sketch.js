var cols,rows;
var w = 60;
var grids = [];
var currentCell;
var stack = [];
var state = document.getElementById("state");
var startCell,endCell;
var findEndPath = false;

function setup() {
    var cnv = createCanvas(600,600);
    cnv.parent("main");
    cols = floor(width/w);
    rows = floor(height/w);
    for (var j = 0; j < rows; j ++) {
        for (var i = 0 ; i < cols; i ++) {
            var cell = new Cell(i,j);
            grids.push(cell);
        }
    }
    currentCell = grids[0];
    state.innerText = "Maze Generate Start";
}

function draw() {
    background(51);
    for (var i = 0; i < grids.length; i ++) {
        grids[i].show();
    }
    if (findEndPath === false) {
        currentCell.visited = true;
        currentCell.highlight();

        var nextCell = currentCell.checkNeighbors("make");
        if (nextCell) {
            nextCell.visited = true;
            stack.push(currentCell);
            removeWalls(currentCell,nextCell);
            currentCell = nextCell;
        }
        else if (stack.length > 0) {
            currentCell = stack.pop();
        }
        if (stack.length === 0) {
            state.innerText = "Maze Generated!!";
            frameRate(5);
            for (var i = 0; i < grids.length; i ++) {
                grids[i].visited = false;
            }
            findEndPath = true;
        }
    }
    else if (findEndPath === true) {
        if (currentCell === endCell) {
            noStroke();
            fill(255,100,255,100);
            rect(currentCell.i*w,currentCell.j*w,w,w);
            noLoop();
            noStroke();
            fill(150,0,0);
            rect(endCell.i*w,endCell.j*w,w,w);
            state.innerText = "END";
        }
        currentCell.visited = true;
        currentCell.highlight();
        var nextCell = currentCell.checkNeighbors("find");
        if (nextCell) {
            nextCell.visited = true;
            stack.push(currentCell);
            currentCell = nextCell;
        }
        else if (stack.length > 0) {
            currentCell = stack.pop();
        }
    }
}

function index(i,j) {
    if (i < 0 || j < 0 || i > cols - 1 || j > rows - 1) {
        return - 1;
    }
    return i + j * cols;
}

function removeWalls(currentCell,nextCell) {
    var x = currentCell.i - nextCell.i;
    if (x === 1) {
        currentCell.walls[3] = false;
        nextCell.walls[1] = false;
    } else if (x === -1) {
        currentCell.walls[1] = false;
        nextCell.walls[3] = false;
    }
    var y = currentCell.j - nextCell.j;
    if (y === 1) {
        currentCell.walls[0] = false;
        nextCell.walls[2] = false;
    } else if (y === -1) {
        currentCell.walls[2] = false;
        nextCell.walls[0] = false;
    }
}
