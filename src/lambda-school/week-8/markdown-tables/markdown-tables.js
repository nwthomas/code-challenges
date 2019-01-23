/*

Convert an array of data into a table in markdown format.Example input:

['name,email', 'emily,emily@email.com', 'mary,maryberry@gbbs.co.uk']

Example output (raw):

|name|email|
|----|-----|
|emily|emily@email.com|
|mary|maryberry@gbbs.co.uk|

Headers will always be strings and the first item in the array. Data always separated with commas, but values may not always be strings. 

*/

function markdownTables(arr) {
  arr.splice(1, 0, arr[0].replace(/[^,]/g, '-'));
  arr.forEach((string, i) => {
    arr[i] = `|${string.toString().split(',').join('|')}|`;
  });
  return arr.join('\n');
}

module.exports = markdownTables;