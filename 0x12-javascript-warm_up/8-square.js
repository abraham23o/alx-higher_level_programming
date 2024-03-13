#!/usr/bin/node

// prints a message depending of the number of arguments passed
const size = parseInt(process.argv[2]);

if (!isNaN(size) && size > 0) {
  for (let i = 0; i < size; i++) {
    let square = '';
    for (let j = 0; j < size; j++) {
      square += 'X';
    }
    console.log(square);
  }
} else {
  console.log('Missing size');
}
