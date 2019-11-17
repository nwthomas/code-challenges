/*

Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less. You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words. If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.

*/

function maxWords(str, len) {
  if (typeof str !== "string" || typeof len !== "number") {
    return null;
  }
  const wordsArr = str.trim().split(" ");
  const final = [];
  let tempStr = "";
  if (wordsArr.filter(num => num.length > len).length) {
    return [];
  }
  for (let i = 0; i < wordsArr.length; i++) {
    const newWord = tempStr.length ? ` ${wordsArr[i]}` : wordsArr[i];
    if ((tempStr + newWord).length <= len) {
      tempStr += newWord;
    } else {
      final.push(tempStr);
      tempStr = "";
      i--;
    }
  }
  tempStr.length && final.push(tempStr);
  return final;
}

module.exports = maxWords;
