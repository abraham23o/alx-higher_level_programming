#!/usr/bin/node

// prints a message depending of the number of arguments passed
const firstArg = process.argv[2];
const toInt = parseInt(firstArg);

if (!isNaN(toInt)) {
  console.log(`My number: ${toInt}`);
} else {
  console.log('Not a number');
}
