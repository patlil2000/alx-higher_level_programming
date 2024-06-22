#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (!Number.isInteger(w) || !Number.isInteger(h)) {
      return {};
    } else if (w <= 0 || h <= 0) {
      return {};
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
