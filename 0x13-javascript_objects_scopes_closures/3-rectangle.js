#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let ix = 0; ix < this.height; ix++) {
      let sxx = '';
      for (let jx = 0; jx < this.width; jx++) {
        sxx += 'X';
      }
      console.log(sxx);
    }
  }
}

module.exports = Rectangle;
