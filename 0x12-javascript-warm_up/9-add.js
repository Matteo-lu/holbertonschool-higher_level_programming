#!/usr/bin/node
const process = require('process');
const value = add(parseInt(process.argv[2]), parseInt(process.argv[3]));

function add (a, b) {
  return (a + b);
}
console.log(value);
