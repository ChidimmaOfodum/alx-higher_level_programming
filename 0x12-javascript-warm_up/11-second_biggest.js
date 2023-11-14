#!/usr/bin/node
const { argv } = require('process');
if (argv.length === 2 || argv.length === 3) console.log(0);
else {
  const numbers = argv.slice(2).sort();
  console.log(parseInt(numbers[numbers.length - 2]));
}
