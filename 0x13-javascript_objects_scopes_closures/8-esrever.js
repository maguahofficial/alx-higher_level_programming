#!/usr/bin/node
exports.esrever = function (list) {
  let lenxx = list.length - 1;
  let ix = 0;
  while ((lenxx - ix) > 0) {
    const aux = list[lenxx];
    list[lenxx] = list[ix];
    list[ix] = aux;
    ix++;
    lenxx--;
  }
  return list;
};
