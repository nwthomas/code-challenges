/*

https://www.codewars.com/kata/53368a47e38700bd8300030d

Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:
list([ {name: 'Bart'}, {name: 'Lisa'}, {name: 'Maggie'} ])
// returns 'Bart, Lisa & Maggie'

list([ {name: 'Bart'}, {name: 'Lisa'} ])
// returns 'Bart & Lisa'

list([ {name: 'Bart'} ])
// returns 'Bart'

list([])
// returns ''

Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.

*/

function list(names) {
  if (names.length === 0) return "";
  if (names.length === 1) return names[0].name;
  let totalPhrase = "";

  for (let i = 0; i < names.length; i++) {
    if (names[i].name === names[names.length - 2].name) {
      return totalPhrase + `${names[i].name} & ${names[i + 1].name}`;
    } else {
      totalPhrase += `${names[i].name}, `;
    }
  }
}

module.exports = list;
