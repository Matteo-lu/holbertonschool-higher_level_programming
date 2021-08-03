#!/usr/bin/node
const process = require('process');
const x = parseInt(process.argv[2]);
const character = 'X';
let i;

if (Number.isNaN(x) || x === undefined) {
  console.log('Missing size');
} else {
  for (i = 0; i < x; i++) {
    console.log(character.repeat(x));
  }
}
