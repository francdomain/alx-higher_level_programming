#!/usr/bin/node
const dict = require('./101-data').dict;

const allList = Object.keys(dict);
const vals = Object.values(dict);
const uniqVal = [...new Set(vals)];
const newDict = {};
for (const j in uniqVal) {
  const list = [];
  for (const k in allList) {
    if (allList[k][1] === uniqVal[j]) {
      list.unshift(allList[k][0]);
    }
  }
  newDict[uniqVal[j]] = list;
}
console.log(newDict);
