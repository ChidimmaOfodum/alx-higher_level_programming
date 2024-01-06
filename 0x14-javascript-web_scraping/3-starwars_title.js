#!/usr/bin/node
// Fetches data from an api

const request = require('request');

if (process.argv[2]) {
  const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
  request(url, async (_, res, body) => {
    if (res && res.statusCode === 200) { console.log(JSON.parse(body).title); }
  });
}
