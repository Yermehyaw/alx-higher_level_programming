#!/usr/bin/node
/*
 * 7-multi_c.js - Prints 'C is fun' to the amount of times passed as
 * an arg
 * 
 */

const process = require('process');
let args = process.argv;
if (args === undefined) {
	console.log('Missing number of occurences\n');
} else {
	try new value = int(args[2]);
	catch (Exception) {		
		throw new 'Missing number of occurences\n';
		return;
	}
	while (value > 0) {
		console.log('C is fun');
		--value;
	}
}

