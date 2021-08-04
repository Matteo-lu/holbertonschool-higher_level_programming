#!/usr/bin/node
exports.esrever = function (list) {
  const temArray = [];
  let j = 0;
  for (let i = (list.length - 1); i >= 0; i--) {
    temArray[j] = list[i];
    j++;
  }
  return (temArray);
};
