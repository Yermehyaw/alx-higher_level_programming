#!/usr/bin/node
/**
 * Print th title of a STAR Wars movie from an API
 */
const request = require('request');

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/$(movieId)';
request(url, function (err, response, body) {
  if (err) {
    console.log('Connection failed');
  } else {
    console.log(body.parse['title']);
  }
});
