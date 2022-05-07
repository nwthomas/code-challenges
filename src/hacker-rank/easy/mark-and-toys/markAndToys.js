/*
Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some. There are a number of different toys lying in front of him, tagged with their prices. Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money. Given a list of toy prices and an amount to spend, determine the maximum number of gifts he can buy.

Note Each toy can be purchased only once.

Example
prices = [1, 2, 3, 4]
k = 7

The budget is 7 units of currency. He can buy items that cost [1, 2, 3] for 6, or [3, 4] for 7 units. The maximum is 3 items.

Function Description

Complete the function maximumToys in the editor below.

maximumToys has the following parameter(s):

int prices[n]: the toy prices
int k: Mark's budget
Returns

int: the maximum number of toys
Input Format

The first line contains two integers, n and k, the number of priced toys and the amount Mark has to spend.
The next line contains n space-separated integers prices[i]

A toy can't be bought multiple times.
*/

function quickSort(n) {
    if (n.length <= 1) {
        return n;
    }

    const pivot = Math.floor(Math.random() * n.length);
    const pivotNum = n[pivot];
    const lower = [];
    const equal = [];
    const higher = [];

    n.forEach((num) => {
        if (num < pivotNum) {
            lower.push(num);
        } else if (num > pivotNum) {
            higher.push(num);
        } else {
            equal.push(num);
        }
    });

    return quickSort(lower).concat(equal).concat(quickSort(higher));
}

function maximumToys(prices, k) {
    const sortedPrices = quickSort(prices);
    let total = 0;
    let purchases = 0;

    sortedPrices.forEach((price) => {
        if (total + price < k) {
            total += price;
            purchases += 1;
        }
    });

    return purchases;
}

module.exports = {
    quickSort,
    maximumToys,
};
