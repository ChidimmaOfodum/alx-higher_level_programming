#!/usr/bin/node
// Displays status of a get request

const request = require('request');

if (process.argv[2]) {
    request(process.argv[2], (err, res, body) => {
        console.log(res && `code: ${res.statusCode}`);
    })
}
