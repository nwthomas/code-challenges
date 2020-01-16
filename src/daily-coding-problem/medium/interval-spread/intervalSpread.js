/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a set of closed intervals, find the smallest set of numbers that covers all the intervals. If there are multiple smallest sets, return any of them.

For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers that covers all these intervals is {3, 6}.
*/

function findIntervalSpread(intervalArray) {
  let final = [],
    firstInterval;
  if (!Array.isArray(intervalArray) || !intervalArray.length) {
    return final;
  }
  intervalArray.forEach(interval => {
    if (!final.length) {
      firstInterval = [interval[1], interval[0]];
      final = [...firstInterval];
    } else {
      interval[0] > final[1] && (final[1] = interval[0]);
      interval[1] < final[0] && (final[0] = interval[1]);
    }
  });
  if (final[0] === firstInterval) {
    return intervalArray[0];
  }
  return final;
}

module.exports = findIntervalSpread;
