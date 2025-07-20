//Note: all the bad words are listed here! all right reserved for their owners
var Filter = require('bad-words'),
    filter = new Filter(),
    badWords = [];

filter.addWords(...badWords);


export {
    filter
}