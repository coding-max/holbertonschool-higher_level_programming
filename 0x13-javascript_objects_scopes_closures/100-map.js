#!/usr/bin/node
console.log(require('./100-data.js').list);
console.log((require('./100-data.js').list).map((a, b) => a * b));
