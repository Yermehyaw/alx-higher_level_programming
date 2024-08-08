/**
 * Liat all movies from an API
 */
const $ = window.$;
$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  // Retrieve json object using jQuery convience ajax get method
  $.get(url, function (response, jsonStatus) { // response is a dict
    if (jsonStatus === 'success') {
      const movies = response.results; // results is a list
      for (const movie of movies) { // movies is a dict of dicts
        const title = $('<li></li>').text(movie.title);
        $('ul#list_movies').append(title);
      }
    }
  }, 'json');
});
