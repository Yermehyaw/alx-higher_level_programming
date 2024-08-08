/**
 * Updates the content of the header elem
 */
const $ = window.$;
$(document).ready(function () {
  $('div#update_header').on('click', function () {
    $('header').text('New Header!!!');
  });
});
