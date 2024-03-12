#!/usr/bin/node

// prints a message depending of the number of arguments passed
const numArgs = process.argv.length - 2;

if (numArgs === 0) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
