#!/usr/bin/node
let nargvr = 0;

exports.logMe = function (item) {
  console.log(nargvr + ': ' + item);
  nargvr++;
};
