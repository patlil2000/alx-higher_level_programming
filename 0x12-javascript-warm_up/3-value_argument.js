#!/usr/bin/node
const arg = process.argv.slice(2);
if (arg[0] === undefined) {
  console.log('No arguments');
} else {
  console.log(arg[0]);
}
