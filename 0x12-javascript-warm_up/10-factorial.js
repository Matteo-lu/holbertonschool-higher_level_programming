#!/usr/bin/node
const process = require('process');
const x = parseInt(process.argv[2]);
const value = factorial(x);

function factorial (n) {
  if (n === 0 || n === 1 || Number.isNaN(x)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(value);
