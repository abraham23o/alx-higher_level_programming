#!/usr/bin/node

// prints a message depending of the number of arguments passed
const firstArg = process.argv[2];
const toInt = parseInt(firstArg);
const strIng = 'C is fun';

if (!isNaN(toInt) && toInt > 0) {
  for (let i = 0; i < toInt; i++) {
    console.log(strIng);
  }
} else {
  console.log('Missing number of occurrences');
}
