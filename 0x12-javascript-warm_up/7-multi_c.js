#!/usr/bin/node

// A script that prints a string several times

const arg = process.argv[2];

const count = parseInt(arg);

const message = 'c is fun';

if (Number.isNaN(count)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < count; i++) {
    console.log(message);
  }
}
