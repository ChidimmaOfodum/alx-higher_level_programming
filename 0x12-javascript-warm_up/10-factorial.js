#!/usr/bin/node
function factorial (num) {
  if (!num) { return 1; }
  return factorial(num - 1) * num;
}
const num = +process.argv[2];

console.log(factorial(num));
