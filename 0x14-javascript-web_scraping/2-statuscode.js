#!/usr/bin/node
/**
 * Print status code of a GET request
 */
const request = require('request');

const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(err);
  }
  console.log(response.ststusCode);
});
