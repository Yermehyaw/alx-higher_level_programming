/**
 * Add, remove and delete list by clicks
 */
const $ = window.$;
$(document).ready(function () {
  $('div#add_item').on('click', function () {
    const item = '<li>Item</li>';
    $('ul.my_list').append(item);
  });
  $('div#remove_item').on('click', function () {
    $('ul.my_list').children().last().remove();
  });
  $('div#clear_list').on('click', function () {
    $('ul.my_list').empty();
  });
});
