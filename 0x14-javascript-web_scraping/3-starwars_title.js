#!/usr/bin/node

const requestURL = 'https://swapi-api.hbtn.io/api/films/';
const movieId = process.argv[2];
const request = require('request');
let obj;

request(requestURL + movieId, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    obj = JSON.parse(body);
    console.log(obj.title);
  }
});
