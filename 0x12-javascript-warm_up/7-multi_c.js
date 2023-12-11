#!/usr/bin/node
const { argv } = require('process');
const occurence = Number(argv[2]);
const display = () => {
  for (let i = 0; i < occurence; i++) {
    console.log('C is fun');
  }
};
isNaN(occurence)
  ? (console.log('Missing number of occurrences'))
  : (display());
