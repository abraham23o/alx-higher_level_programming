#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./2-statuscode.js <url>');
  process.exit(1);
}

const url = process.argv[2];

request.get(url, (err, response) => {
  if (err) {
    console.error(err);
  } else {
    console.log('code: ', response.statusCode);
  }
});
