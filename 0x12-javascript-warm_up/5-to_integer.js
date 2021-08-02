#!/usr/bin/node
const process = require('process');
const prhase = 'My number:';
const value = parseInt(process.argv[2]);

if (Number.isNaN(value)) {
  console.log('Not a number');
} else {
  console.log(prhase, parseInt(process.argv[2]));
}
