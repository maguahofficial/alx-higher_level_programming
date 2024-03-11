#!/usr/bin/node
function factorial (nx) {
  if (nx < 0) {
    return (-1);
  }
  if (nx === 0 || isNaN(nx)) {
    return (1);
  }
  return (nx * factorial(n - 1));
}

console.log(factorial(Number(process.argv[2])));
