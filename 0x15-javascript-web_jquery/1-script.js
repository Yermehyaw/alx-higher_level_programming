/**
 * Update the color of the text in the headr elem to red
 */
const $ = window.$;
$(document).ready(function () {
  const header = $('header');
  header.css('color', 'red');
});
