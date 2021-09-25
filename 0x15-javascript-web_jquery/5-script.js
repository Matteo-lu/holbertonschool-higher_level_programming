#!/usr/bin/node

$(function () {
  const txt1 = '<li>Item</li>';
  $('#add_item').on('click', function () {
    $('.my_list').append(txt1);
  });
});
