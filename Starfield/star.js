
function Star() {
    this.x = random(-width,width);
    this.y = random(-height,height);
    this.z = random(width);
    this.zpos = this.z;

    this.update = function() {
        this.z = this.z - speed;
        if (this.z < 1) {
            this.z = width;
            this.x = random(-width,width);
            this.y = random(-height,height);
            this.zpos = this.z;
        }
    }

    this.show = function() {
        fill(255);
        noStroke();

        var xspeed = map(this.x / this.z, 0, 1, 0, width);
        var yspeed = map(this.y / this.z, 0, 1, 0, height);
        var radius = map(this.z, 0, width, 16, 0);
        ellipse(xspeed, yspeed, radius, radius);

        var xpos = map(this.x / this.zpos, 0, 1, 0, width);
        var ypos = map(this.y / this.zpos, 0, 1, 0, height);

        this.zpos = this.z;

        stroke(255);
        line(xpos, ypos, xspeed, yspeed);
    }
}
