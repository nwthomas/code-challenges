

const { threeSum } = require('./threeSum');
const assert = require('assert');

const shortList = [-2, -2, -1, 0, 0, 3, 3, 4, 5, 5]
const longList = [-8, -8, -5, -3, -2, -2, -1, 0, 0, 3, 3, 4, 5, 5, 8, 9, 9, 10]

describe('threeSum', () => {
    it('should return an empty array if the input array has not three sum triplets', () => {
        assert.deepEqual(threeSum([1, 2]), []);
    });

    it('should return a short array of triplets that sum to 0', () => {
        assert.deepEqual(threeSum(shortList), [[-2, -2, 4], [-1, -2, 3] ]);
    });

    it('should return a long array of triplets that sum to 0', () => {
        assert.deepEqual(threeSum(longList), [[-2, -8, 10], [-1, -8, 9], [-8, 0, 8], [-8, 3, 5], [-3, -5, 8], [-5, 0, 5], [-2, -3, 5], [-1, -3, 4], [-3, 0, 3], [-2, -2, 4], [-1, -2, 3]]);
    });
});