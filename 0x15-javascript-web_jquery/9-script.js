#!/usr/bin/node

$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (data) {
      $('#hello').append(data.hello);
    }
  });
});
