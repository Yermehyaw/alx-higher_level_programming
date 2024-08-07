#!/usr/bin/node
/**
 * Print contents of a file to console
 */
const fs = require('fs');

const fileName = process.argv[2];/* [2] is the first command arg in shell */
const toWrite = process.argv[3];
fs.writeFile(fileName, toWrite, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  }
});
