#!/usr/bin/node

let count = 0; // This counter is preserved in the closure of the `logMe` function

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++; // Increment the count after printing
};
