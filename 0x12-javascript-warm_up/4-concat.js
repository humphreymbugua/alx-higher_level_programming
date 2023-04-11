#!/usr/bin/node
if (process.argv[2] !== undefined && process.argv[3] !== undefined) {
  console.log('${process.argv[2]} is ${process.argv[3]}');
} else {
  console.log('Please provide at least two arguments.');
}
