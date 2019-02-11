/*

Write a function that given an array of objects will return a single 'merged' object, where duplicate keys have the last value given.
For example: 

[
{1: '1', 2: '2', 3: '3'},
{3: '4', 4: '4', 5: '6'},
{5: '5', 6: '6', 7: '7'}
];

Should return:

{1: '1', 2: '2': 3: '4', 4: '4', 5: '5', 6: '6', 7: '7'}

...where the value of 5 is '5' because '5' it was the last given value for that key.

*/

function mergeObjects(arr) {
  let finalObj = {};
  arr.forEach(obj => {
    Object.assign(finalObj, obj);
  });
  return finalObj;
}

module.exports = mergeObjects;
