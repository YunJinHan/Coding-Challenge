function Cell(i,j) {
    this.i = i;
    this.j = j;
    this.walls = [true,true,true,true];
    this.visited = false;

    this.checkNeighbors = function(type) {
        var neighbors = [];

        var top = grids[index(i,j - 1)];
        var right = grids[index(i + 1,j)];
        var bottom = grids[index(i,j + 1)];
        var left = grids[index(i - 1,j)];

        if (index(i + 1,j) == -1 && index(i,j + 1) == -1) {
            endCell = this;
        }
        if (index(i, j - 1) == -1 && index(i - 1,j) == -1) {
            startCell = this;
        }

        if (type === "make") {
            if (top && !top.visited) {
                neighbors.push(top);
            }
            if (right && !right.visited) {
                neighbors.push(right);
            }
            if (bottom && !bottom.visited) {
                neighbors.push(bottom);
            }
            if (left && !left.visited) {
                neighbors.push(left);
            }
        }
        else if (type === "find") {
            if (top && !top.visited && !this.walls[0]) {
                neighbors.push(top);
            }
            if (right && !right.visited && !this.walls[1]) {
                neighbors.push(right);
            }
            if (bottom && !bottom.visited && !this.walls[2]) {
                neighbors.push(bottom);
            }
            if (left && !left.visited && !this.walls[3]) {
                neighbors.push(left);
            }
        }
        if (neighbors.length > 0) {
            var nextDirection = floor(random(0,neighbors.length));
            return neighbors[nextDirection];
        }
        else {
            return undefined;
        }
    }

    this.highlight = function () {
        var x = this.i * w;
        var y = this.j * w;
        noStroke();
        fill(0,0,255,100);
        rect(x,y,w,w);
    }

    this.show = function() {
        var x = this.i*w;
        var y = this.j*w;
        stroke(255);
        if (this.walls[0]) {
            line(x, y, x + w, y);
        }
        if (this.walls[1]) {
            line(x + w, y, x + w, y + w);
        }
        if (this.walls[2]) {
            line(x + w, y + w, x, y + w);
        }
        if (this.walls[3]) {
            line(x, y + w, x, y);
        }
        if (this.visited) {
            noStroke();
            fill(255,100,255,100);
            rect(x,y,w,w);
        }
    }
}
