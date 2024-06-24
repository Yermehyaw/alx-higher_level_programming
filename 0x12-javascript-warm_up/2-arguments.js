#!/usr/bin/node
const process = require('process');
let args = process.argv;
if (args !== undefined) {
	console.log('Argument found');
} else {
	console.log('No argument');
}

