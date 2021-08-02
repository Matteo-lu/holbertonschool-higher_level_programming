#!/usr/bin/node
const process = require('process');
const value;

function add (a, b) {
  return (a + b);
}

value = add(parseInt(process.argv[2]), parseInt(process.argv[3]));
console.log(value);
