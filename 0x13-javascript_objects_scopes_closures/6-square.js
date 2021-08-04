#!/usr/bin/node
const SquareC = require('./5-square');
class Square extends SquareC {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
