#!/usr/bin/node
const x = process.argv[2];
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < Number(x)) {
    console.log('C is fun');
    i++;
  }
}
