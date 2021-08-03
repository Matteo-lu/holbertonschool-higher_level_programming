#!/usr/bin/node
const process = require('process');
const myArray = [];
let max;
let i;
let j = 2;

if (process.argv.length < 3) {
  console.log(0);
} else if (process.argv.length < 4) {
  console.log(0);
} else {
  for (i = 0; i < (process.argv.length - 2); i++) {
    myArray[i] = parseInt(process.argv[j]);
    j++;
  }
  max = Math.max.apply(null, myArray);
  myArray.splice(myArray.indexOf(max), 1);
  max = Math.max.apply(null, myArray);
  console.log(max);
}
