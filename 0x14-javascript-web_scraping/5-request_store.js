#!/usr/bin/node

const requestURL = process.argv[2];
const filePath = process.argv[3];
const request = require('request');
const fs = require('fs');
let obj;

request(requestURL, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    obj = body;
    try {
      fs.writeFileSync(filePath, obj);
    } catch (err) {
      console.dir(err);
    }
  }
});
