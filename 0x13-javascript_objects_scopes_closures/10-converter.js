#!/usr/bin/node

exports.converter = function (base) {
  function nuBase (num) {
    return num.toString(base);
  }
  return nuBase;
};
