#!/usr/bin/node

//  a script that computes and prints a factorial

function factorial (n) {
  if (n < 0) {
    return 1;
  } else if (n === 0 || isNaN(n)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const arg = parseInt(process.argv[2]);

const result = factorial(arg);

console.log(result);
