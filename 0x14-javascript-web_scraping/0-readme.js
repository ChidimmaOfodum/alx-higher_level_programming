#!/usr/bin/node
// Reading and printing from a file

const fs = require('fs');

if (process.argv[2]) {
  fs.readFile(process.argv[2], 'utf-8', (err, data) => {
    console.log(err || data);
  });
}
