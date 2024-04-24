#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./3-starwars_title.js <movieId>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error('Failed to retrieve movie information. Status code:', response.statusCode);
  } else {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  }
});