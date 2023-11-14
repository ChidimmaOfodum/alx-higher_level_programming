#!/usr/bin/node
const { argv } = require('process');
if (argv.length === 2 || argv.length === 3) console.log(0);
else {
  let numbers = argv.slice(2).sort();
  numbers = numbers.filter((x, i) => numbers.lastIndexOf(x) === i);
  console.log(parseInt(numbers[numbers.length - 2]) || parseInt(numbers[0]));
}
