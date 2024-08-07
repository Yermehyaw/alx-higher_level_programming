/**
 * Toggle betweeb two CSS classes on an element when clicked
 */
const $ = window.$;
$(document).ready(function () {
  const toggle_header = $('div#toggle_header');
  toggle_header.addClass('red');
  toggle_header.on('click', function () {
    $(this).toggleClass('green');
  });
});
