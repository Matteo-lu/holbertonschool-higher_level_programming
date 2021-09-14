#!/usr/bin/node

const fs = require('fs');
const fileName = process.argv[2];
const stringToWrite = process.argv[3];

try {
  fs.writeFileSync(fileName, stringToWrite);
} catch (err) {
  console.dir(err);
}
