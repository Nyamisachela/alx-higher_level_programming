#!/usr/bin/node

//  a script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop

const lines = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

let output = '';

for (let i = 0; i < lines.length; i++) {
  output += lines[i] + '\n';
}
console.log(output.trim());
