#!/usr/bin/node
const process = require('process');
const arguments = process.argv;
let myArray = [];
let max;
let i;
let j = 2;

if (arguments.length < 3) {
  console.log(0)
} else if (arguments.length < 4) {
  console.log(0)
} else {
  for (i = 0; i < (arguments.length - 2); i++) {
    myArray[i] = parseInt(arguments[j]);
    j++;
  }
  max = Math.max.apply(null, myArray);
  myArray.splice(myArray.indexOf(max), 1);
  max = Math.max.apply(null, myArray);
  console.log(max)
}
