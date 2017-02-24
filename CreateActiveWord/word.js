function Word(x,y) {
    this.pos = createVector(random(width),random(height));
    this.target = createVector(x,y);
    this.vel = p5.Vector.random2D();
    this.acc = createVector();
    this.r = 8;
    this.maxSpeed = 8;
    this.maxForce = 0.5;
}

Word.prototype.behaviors = function() {
    var arrive = this.arrive(this.target);
    var mouse = createVector(mouseX,mouseY);
    var flee = this.flee(mouse);

    arrive.mult(1);
    flee.mult(2);

    this.applyForce(arrive);
    this.applyForce(flee);
}

Word.prototype.applyForce = function(force) {
    this.acc.add(force);
}

Word.prototype.update = function() {
    this.pos.add(this.vel);
    this.vel.add(this.acc);
    this.acc.mult(0);
}

Word.prototype.show = function() {
    stroke(255);
    strokeWeight(8);
    point(this.pos.x,this.pos.y);
}

Word.prototype.arrive = function(target) {
    var desired = p5.Vector.sub(target, this.pos);
    var distance = desired.mag();
    var speed = this.maxSpeed;
    if (distance < 100) {
        speed = map(distance, 0, 100, 0, this.maxSpeed);
    }
    desired.setMag(speed);
    var steer = p5.Vector.sub(desired, this.vel);
    steer.limit(this.maxForce);
    return steer;
}

Word.prototype.flee = function(target) {
    var desired = p5.Vector.sub(target, this.pos);
    var distance = desired.mag();
    if (distance < 50) {
        desired.setMag(this.maxSpeed);
        desired.mult(-1);
        var steer = p5.Vector.sub(desired, this.vel);
        steer.limit(this.maxForce);
        steer.mult(-1);
        return steer;
    }
    return createVector(0,0);
}
