function Snake() {
    this.x = 0;
    this.y = 0;
    this.xspeed = 0;
    this.yspeed = 0;
    this.totalLength = 0;
    this.tail = [];

    this.init = function() {
        this.x = 0;
        this.y = 0;
        this.xspeed = 0;
        this.yspeed = 0;
        this.totalLength = 0;
        this.tail = [];
        pickLocation();
        var state = document.getElementById("state");
        state.innerText = "Game Over .. Restart ?";
    }

    this.eat = function(position) {
        var d = dist(this.x, this.y, position.x, position.y);
        if (d < 1) {
            this.totalLength ++;
            var state = document.getElementById("state");
            state.innerText = "Record : " + this.totalLength;
            return true;
        } else {
            return false;
        }
    }

    this.dir = function(x,y) {
        this.xspeed = x;
        this.yspeed = y;
    }

    this.gameOver = function() {
        for (var i = 0; i < this.tail.length; i ++) {
            var pos = this.tail[i];
            var d = dist(this.x, this.y, pos.x, pos.y);
            if (d < 1) {
                this.init();
            }
        }
    }

    this.update = function () {
        if (this.totalLength === this.tail.length) {
            for (var i = 0; i < this.tail.length - 1; i ++) {
                this.tail[i] = this.tail[i + 1];
            }
        }
        this.tail[this.totalLength - 1] = createVector(this.x, this.y);

        this.x = this.x + this.xspeed*scl;
        this.y = this.y + this.yspeed*scl;

        this.x = constrain(this.x, 0, width-scl);
        this.y = constrain(this.y, 0, height-scl);
    }

    this.show = function () {
        fill(255);
        for (var i = 0; i < this.tail.length; i ++) {
            rect(this.tail[i].x, this.tail[i].y, scl, scl);
        }

        fill(255);
        rect(this.x, this.y, scl, scl);
    }

}
