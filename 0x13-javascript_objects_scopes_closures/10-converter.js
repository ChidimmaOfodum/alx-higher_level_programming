#!/usr/bin/node
exports.converter = function (base) {
    return (x) => parseInt(x, 10).toString(base); 
}
