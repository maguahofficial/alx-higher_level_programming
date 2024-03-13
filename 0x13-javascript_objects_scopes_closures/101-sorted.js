#!/usr/bin/node
const dict = require('./101-data').dict;

const totalistxx = Object.entries(dict);
const valsxx = Object.values(dict);
const valsUniqxx = [...new Set(valsxx)];
const newDictxx = {};
for (const jx in valsUniqxx) {
  const list = [];
  for (const kx in totalistxx) {
    if (totalist[kx][1] === valsUniqxx[jx]) {
      list.unshift(totalist[kx][0]);
    }
  }
  newDict[valsUniqxx[jx]] = list;
}
console.log(newDictxx);
