/**
 * Add a li elem to a tag when clicked
 */
const $ = window.$;
$(document).ready(function () {
  const item1 = '<li>Item</li>';
  $('div#add_item').on('click', function () {
    $('ul.my_list').append(item1);
  });
});
