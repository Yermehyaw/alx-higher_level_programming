/**
 * Adds a CSS class to an element when clicked
 */
const $ = window.$;
$(document).ready(function () {
  $('div#red_header').on('click', function () {
    $(this).addClass('red');
  });
});
