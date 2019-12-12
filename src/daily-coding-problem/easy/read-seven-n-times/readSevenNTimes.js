/*

Good morning! Here's your coding interview problem for today.

This problem was asked Microsoft.

Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.

*/

function readN(n, file) {
  if (typeof n !== "number" || typeof file !== "string" || n < 0) {
    return null;
  }
  let _currentFile = file;
  const final = [];
  for (let i = 0; i < n; i++) {
    final.push(read7(_currentFile));
    _currentFile = _currentFile.slice(7, _currentFile.length);
  }
  return final;
}

function read7(file) {
  if (typeof file !== "string") {
    return null;
  }
  return file.slice(0, 7);
}

module.exports = {
  readN,
  read7
};
