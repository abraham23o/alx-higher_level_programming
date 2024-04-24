#!/usr/bin/node

const request = require('request');
const fs = require('fs');

if (process.argv.length !== 4) {
  console.error('Usage: ./5-request_store <url> <filepath>');
  process.exit(1);
}

const urlApi = process.argv[2];
const filePath = process.argv[3];

request.get(urlApi, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error('Failed to retrieve movie information. Status code:', response.statusCode);
  } else {
    fs.writeFileSync(filePath, body, 'utf-8');
  }
});
