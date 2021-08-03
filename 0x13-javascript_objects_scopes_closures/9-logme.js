#!/usr/bin/node
let pichu = 0;
exports.logMe = function (item) {
  console.log(pichu + ': ' + item);
  pichu++;
};
