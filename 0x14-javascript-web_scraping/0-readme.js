#!/usr/bin/node

const fs = require('fs');
const fileName = process.argv[2];

try {
  const data = fs.readFileSync(fileName, 'utf-8');
  console.log(data);
} catch (err) {
  console.dir(err);
}
