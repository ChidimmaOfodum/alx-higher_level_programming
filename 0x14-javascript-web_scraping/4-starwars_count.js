#!/usr/bin/node
// A script that prints the number of movies when a particular character is present

const request = require('request');

if (process.argv[2]) {
  const url = 'https://swapi-api.alx-tools.com/api/films';
  const targetCharUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
  request(url, (_, res, body) => {
    if (res && res.statusCode === 200) {
      let count = 0;
      const { results } = JSON.parse(body);
      for (const item of results) {
        const { characters } = item;
        count = characters.includes(targetCharUrl) ? count + 1 : count;
      }
      console.log(count);
    }
  });
}
