#!/usr/bin/node

const process = require('process');
let args = process.argv;
if (args.length < 4) {
	console.log(args[2] + 'is undefined');
} else {
	let concatStr = args[2] + 'is' + args[3];
}

