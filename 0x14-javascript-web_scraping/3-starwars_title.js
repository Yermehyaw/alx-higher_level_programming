#!/usr/bin/node
/**
 * Print the title of a STAR Wars movie from an API
 */
const request = require('request');

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
request.get(url, function (err, response, body) {
  if (err) {
    return console.log('Connection failed');
  } else {
    const movieTitle = JSON.parse(body);
    console.log(movieTitle.title);
  }
});
