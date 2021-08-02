#!/usr/bin/node
const process = require('process');
const x = process.argv[2];
const prhase = 'C is fun';
let i;

if (x === undefined) {
  console.log('Missing number of occurrences');
}
for (i = 0; i < x; i++) {
  console.log(prhase);
}
