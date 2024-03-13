#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let ix= 0; ix < this.height; ix++) {
      let sxx = '';
      for (let jx = 0; jx < this.width; jx++) {
        sxx += c;
      }
      console.log(sxx);
    }
  }
}

module.exports = Square;
