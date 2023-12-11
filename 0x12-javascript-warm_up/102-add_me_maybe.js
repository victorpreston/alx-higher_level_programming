#!/usr/bin/node
exports.addMeMaybe = function addMeMaybe (number, theFunction) {
  return theFunction(++number);
};
