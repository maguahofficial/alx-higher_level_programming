#!/usr/bin/node
function add (a, b) {
  const cx = a + b;
  console.log(cx);
}

add(Number(process.argv[2]), Number(process.argv[3]));
