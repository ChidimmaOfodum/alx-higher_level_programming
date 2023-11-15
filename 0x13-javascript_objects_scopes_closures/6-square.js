#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const char = c === undefined ? 'X' : c;

    for (let i = 0; i < this.height; i++) {
      let result = '';
      for (let j = 0; j < this.width; j++) {
        result += char;
      }
      console.log(result);
    }
  }
};
