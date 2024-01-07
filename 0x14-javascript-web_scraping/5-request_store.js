#!/usr/bin/node
// Gets the content of a webpage and writes to a file

const fs = require('fs');
const request = require('request');
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
