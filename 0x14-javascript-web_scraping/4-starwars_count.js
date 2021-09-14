#!/usr/bin/node

const requestURL = process.argv[2];
const characterId = '18';
const request = require('request');
let obj;
let countChar = 0;
let i;
let j;

request(requestURL, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    obj = JSON.parse(body);
    for (i = 0; i < obj.results.length; i++) {
      for (j = 0; j < obj.results[i].characters.length; j++) {
        if (obj.results[i].characters[j].search(characterId) !== -1) {
          countChar += 1;
        }
      }
    }
    console.log(countChar);
  }
});
