#!/usr/bin/node

// searches the second biggest integer in the list of arguments

const args = process.argv.slice(2);

if (args.length < 2) {
  // If less than two integers are provided, the requirement is to print 0
  console.log(0);
} else {
  const numbers = args.map(Number);

  let largest = -Infinity;
  let secondLargest = -Infinity;

  for (const number of numbers) {
    if (number > largest) {
      secondLargest = largest;
      largest = number;
    } else if (number > secondLargest) {
      secondLargest = number;
    }
  }
  console.log(secondLargest);
}
