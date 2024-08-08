/**
 * Update the text in an elem with json returned from an API
 */
const $ = window.$;
$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  // Retrieve json object using jQuery convience ajax get method
  $.get(url, function (response, jsonStatus) {
    if (jsonStatus === 'success') {
      const name = response.name;
      $('div#character').text(name); // update the desired elem
    }
  }, 'json');
});
