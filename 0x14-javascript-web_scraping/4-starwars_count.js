#!/usr/bin/node
// A script that prints the number of movies when a particular character is present

const request = require('request');

if (process.argv[2]) {
    const url = "https://swapi-api.alx-tools.com/api/people/18";
    request(url, (err, res, body) => {
        console.log(JSON.parse(body).films.length)
    })
}
