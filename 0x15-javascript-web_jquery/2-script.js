/**
 * updates the text color of the <header> element to red
 *  when the user clicks on the tag DIV#red_header
 */
const $ = window.$
$(document).ready(function () {
  $('div#red_header').on('click', function () {
    $(this).css('color', 'red');
  });
});
