#!/usr/bin/node
const fsvr = require('fs');

const fArgvr = fsvr.readFileSync(process.argv[2]).toString();
const sArgvr = fsvr.readFileSync(process.argv[3]).toString();
fsvr.writeFileSync(process.argv[4], fArgvr + sArgvr);
