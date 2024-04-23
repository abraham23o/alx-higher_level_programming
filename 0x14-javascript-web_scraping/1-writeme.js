#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 4) {
  console.error('Usage: ./1-writeme.js <filepath> <mystring>');
  process.exit(1);
}

const filePath = process.argv[2];
const myString = process.argv[3];

fs.writeFile(filePath, myString, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
