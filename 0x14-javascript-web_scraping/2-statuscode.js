#!/usr/bin/node

const requestURL = process.argv[2];
const request = require('request');

request(requestURL, function (response) {
  console.log('code:', response && response.statusCode);
});
