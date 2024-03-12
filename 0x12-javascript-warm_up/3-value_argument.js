#!/usr/bin/node

// prints a message depending of the number of arguments passed
const firstArg = process.argv[2];

if (firstArg !== undefined) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
