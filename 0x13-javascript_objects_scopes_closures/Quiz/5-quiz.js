#!/usr/bin/node
let b = 1;

function myFunction(a) {
    console.log(a + b);
    b = a;
}

myFunction(3);
myFunction(4);
