#!/usr/bin/node

const requestURL = 'https://swapi-api.hbtn.io/api/films/';
const request = require('request');
let obj;
const filmID = process.argv[2];
let j;
let characterObj;

request(requestURL + filmID, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    obj = JSON.parse(body);
    for (j = 0; j < obj.characters.length; j++) {
      request(obj.characters[j], function (error, response, body) {
        if (!error && response.statusCode === 200) {
          characterObj = JSON.parse(body);
          console.log(characterObj.name);
        }
      });
    }
  }
});
