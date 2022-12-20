#!/usr/bin/node
const x = process.argv[2];
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < Number(x)) {
    console.log('X'.repeat(Number(x)));
    i++;
  }
}
