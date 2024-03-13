#!/usr/bin/node

// gets the commandline args
const args = process.argv.slice(2);

const count = args.length;

// check the number of arguments if 1 or 0 print 0
if (count <= 1) {
  console.log(0);
} else {
  const sortedInt = args.map(Number).sort((a, b) => b - a);
  const secondInt = sortedInt[1];
  console.log(secondInt);
}
