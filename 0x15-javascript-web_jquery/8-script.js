#!/usr/bin/node

$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: function (data) {
      for (const movie in data.results) {
        const movieName = '<li>' + data.results[movie].title + '</li>';
        $('#list_movies').append(movieName);
      }
    }
  });
});
