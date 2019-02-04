/*

Find the first item that occurs an even number of times in an array.

Remember to handle multiple even-occurrence items and return the first one.

Return null if there are no even-occurrence items.

Example usage:
const arr = [1, 7, 2, 4, 5, 6, 8, 9, 6, 4];
console.log(evenOccurrence(arr)); // <--- 4 

*/

function evenOccurrence(arr) {
  const found = {};
  let firstEven = [];
  arr.forEach(item => {
    if (Object.keys(found).includes(item.toString())){
      return firstEven.unshift([`${item}`]);
    } else {
      found[`${item}`] = 1; 
    }
  });
  return firstEven.length > 0 ? Number(firstEven[0]) : null;
}

module.exports = evenOccurrence;