#!/usr/bin/node
function factorial (num) {
  if (num === 0) { return 0; }
  if (num === 1 || isNaN(num)) { return 1; }
  return factorial(num - 1) * num;
}
const num = +process.argv[2];

console.log(factorial(num));
