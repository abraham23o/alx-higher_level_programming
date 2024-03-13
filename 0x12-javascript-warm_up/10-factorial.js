#!/usr/bin/node

const para = parseInt(process.argv[2]);

const _factorial = function (n) {
// factorial of NaN and 0 is 1
  if (isNaN(n) || n === 0) {
    return 1;
  } else {
    return n * _factorial(n - 1);
  }
};

console.log(_factorial(para));
