#!/usr/bin/node

const firstArg = parseInt(process.argv[2]);
const secondArg = parseInt(process.argv[3]);

function add (a, b) {
  return a + b;
}

if (!isNaN(firstArg) && !isNaN(secondArg)) {
  const result = add(firstArg, secondArg);
  console.log(result);
} else {
  console.log('NaN');
}
