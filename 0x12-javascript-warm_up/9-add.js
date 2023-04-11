#!/usr/bin/node
function add(a, b) {
   return Number(a) + Number(b);
}

if (process.argv[2] === undefined || process.argv[3] === undefined) {
  console.log('NaN');
} else {
  console.log(add(process.arg[2], process.arg[3]));
}
