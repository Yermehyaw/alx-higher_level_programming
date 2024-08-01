#!/usr/bin/node
/**
 * Print  the number of movies where the character “Wedge Antilles” is present
 * using a REST API
 */
const request = require('request');

const url = process.argv[2];
characterURL = 'https://swapi-api.alx-tools.com/api/people/18/';
request(url, function (error, response, body) {
  if (error || response.statusCode >= 400) {
    return console.log('Connection failed');
  }
  let noOfFeatures = 0;
  const jsonBody = JSON.parse(body);
  const allFilms = jsonBody.results;  /* a list of dicts */
  for (const movieDetail of allFilms) {
    const characters = movieDetail.characters /* a list */
    for (const character of characters) {
      if (character == characterURL) {
        noOfFeatures += 1;
      }
    }
  }
  return console.log(noOfFeatures)
});

