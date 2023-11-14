#!/usr/bin/node
const size = process.argv[2];
if (size) {
  for (let i = 0; i < size; i++) {
    let string = '';
    for (let j = 0; j < size; j++) {
      string += 'X';
    }
    console.log(string);
  }
} else {
  console.log('Missing size');
}
