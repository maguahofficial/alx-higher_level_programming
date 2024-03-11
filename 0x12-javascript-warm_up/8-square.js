#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const x = Number(process.argv[2]);
  let ix = 0;
  while (ix < x) {
    console.log('X'.repeat(x));
    ix++;
  }
}
