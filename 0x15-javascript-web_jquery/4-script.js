/**
 * Toggle betweeb two CSS classes on an element when clicked
 */
const $ = window.$;
$(document).ready(function () {
  const toggleHeader = $('div#toggle_header');
  toggleHeader.addClass('red');
  toggleHeader.on('click', function () {
    $(this).toggleClass('green');
  });
});
