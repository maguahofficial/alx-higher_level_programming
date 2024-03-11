#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let ix = 0; ix < x; ix++) {
    theFunction();
  }
};
