#!/usr/bin/node
const list = process.argv.splice(2);
if (list.length === 0 || list.length === 1) {
  console.log(0);
} else {
  const newList = list.sort((a, b) => b - a);
  console.log(newList[1]);
}
