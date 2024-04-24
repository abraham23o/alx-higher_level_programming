#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./4-starwars_count.js <url>');
  process.exit(1);
}

const url = process.argv[2];
let movies = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);
    movieData.results.forEach(function (result) {
      result.characters.forEach(function (character) {
        const split = character.split('/');
        if (split[split.length - 2] === '18') {
          movies++;
        }
      });
    });
    console.log(movies);
  }
});
