#!/usr/bin/node

// Writes to a file
const fs = require('fs');

if (process.argv.length === 4) {
  const fileName = process.argv[2];
  const data = process.argv[3];
  fs.writeFile(fileName, data, (err) => {
    if (err) { console.log(err); }
  });
}
