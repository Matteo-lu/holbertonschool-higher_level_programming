#!/usr/bin/node

const requestURL = process.argv[2];
const request = require('request');

request
  .get(requestURL)
  .on('response', function(response) {
    console.log('code:', response.statusCode) // 200
  });
