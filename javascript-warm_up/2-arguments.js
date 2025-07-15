#!/usr/bin/node
const argsCnt = process.argv.length - 2;

if (argsCnt === 0) {
  console.log('No argument');
} else if (argsCnt === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
