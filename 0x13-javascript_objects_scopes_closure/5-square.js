#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size); // Call the superclass constructor with both arguments as size
  }
}

module.exports = Square;
