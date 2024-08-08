/**
 * Fetch data from an API and display a particular string
 */
const $ = window.$;
$(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.get(url, function (response, jsonStatus) {
    if (jsonStatus === 'success') {
      const hello = response.hello;
      $('div#hello').text(hello);
    }
  }, 'json');
});
