#!/usr/bin/node
exports.esrever = function (list) {
  const rev = [];
  for (let i = 0; i < list.length; i++) {
    rev[list.length - i - 1] = list[i];
  }
  return rev;
};
