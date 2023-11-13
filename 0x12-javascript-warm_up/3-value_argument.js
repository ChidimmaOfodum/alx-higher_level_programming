#!/usr/bin/node
const { argv } = require('process');
const len = argv.length;
if (len === 2) console.log('No argument');
else console.log(process.argv[2]);
