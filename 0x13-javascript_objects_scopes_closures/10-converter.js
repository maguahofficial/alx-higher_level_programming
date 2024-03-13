#!/usr/bin/node

exports.converter = function (base) {
  return function (numvr) {
    return numvr.toString(base);
  };
};
