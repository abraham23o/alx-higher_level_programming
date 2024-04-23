#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-readme.js <filepath>');
  process.exit(1);
}

const filePath = process.argv[2];

// Read the content of the file in utf8
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
