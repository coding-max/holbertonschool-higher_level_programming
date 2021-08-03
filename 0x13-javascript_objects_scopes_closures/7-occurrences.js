#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let pichu = 0;
  for (const i in list) {
    if (list[i] === searchElement) {
      pichu++;
    }
  }
  return pichu;
};
