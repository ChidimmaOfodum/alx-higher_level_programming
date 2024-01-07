#!/usr/bin/node
// A script that prints the number of movies when a particular character is present

const request = require('request');

if (process.argv[2]) {
  request(process.argv[2], (_, res, body) => {
    if (res && res.statusCode === 200) {
      let count = 0;
      const { results } = JSON.parse(body);
      for (const item of results) {
        const { characters } = item;
        count = characters.find((x) => x.endsWith('/18/')) ? count + 1 : count;
      }
      console.log(count);
    }
  });
}
