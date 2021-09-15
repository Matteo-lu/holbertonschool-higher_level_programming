#!/usr/bin/node

const requestURL = process.argv[2];
const request = require('request');
let obj;
let countTask = 0;
let i;
let j;
const newJSON = {};

request(requestURL, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    obj = JSON.parse(body);
    for (j = 1; j <= obj[obj.length - 1].userId; j++) {
      for (i = 0; i < obj.length; i++) {
        if (obj[i].userId === j && obj[i].completed === true) {
          countTask += 1;
        }
      }
      newJSON[j.toString()] = countTask;
      countTask = 0;
    }
    console.log(newJSON);
  }
});
