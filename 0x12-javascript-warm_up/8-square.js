#!/usr/bin/node

//  a script that prints a square

const square = process.argv[2];

const size = parseInt(square);

if (Number.isNaN(size) || size <= 0) {
  if (Number.isNaN(size)) {
    console.log('Missing size');
  }
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
