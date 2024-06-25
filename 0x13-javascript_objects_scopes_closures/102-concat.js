#!/usr/bin/node
const arg = process.argv;
const fs = require('fs');
try {
  const data1 = fs.readFileSync(arg[2], 'utf-8');
  const data2 = fs.readFileSync(arg[3], 'utf-8');
  const combinedData = data1 + data2;
  fs.writeFileSync(arg[4], combinedData, 'utf-8');
} catch (error) {
  console.log(error);
}
