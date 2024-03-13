#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOccurrencesxx = 0;
  for (let ix = 0; ix < list.length; ix++) {
    if (searchElement === list[ix]) {
      nOccurrencesxx++;
    }
  }
  return nOccurrencesxx;
};
