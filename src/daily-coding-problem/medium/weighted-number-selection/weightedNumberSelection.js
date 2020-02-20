/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Triplebyte.

You are given n numbers as well as n probabilities that sum up to 1. Write a function to generate one of the numbers with its corresponding probability.

For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2], your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.

You can generate random numbers between 0 and 1 uniformly.
*/

const addZeros = (num, length) => {
    let newNum = `${num}`.split(".")[1];
    if (newNum.length === length) {
        return Number(newNum);
    } else {
        while (newNum.length < length) {
            newNum += "0";
        }
        return Number(newNum);
    }
};

const findRandomArrayLength = probabilities => {
    const randomArrayLength = probabilities.reduce(
        (accumulator, probability) => {
            const length = `${probability}`.split(".")[1].length;
            if (length > accumulator) {
                return length;
            } else {
                return accumulator;
            }
        },
        0
    );
    return randomArrayLength;
};

const generateWeightedNumberArray = (numberArray, probabilities) => {
    const newNumberArray = [];
    numberArray.forEach((num, index) => {
        for (let i = 0; i < probabilities[index]; i++) {
            newNumberArray.push(num);
        }
    });
    return newNumberArray;
};

const generateWeightedRandomNumber = (numberArray, probabilities) => {
    if (!Array.isArray(numberArray)) {
        throw new TypeError("The first argument must be an array of numbers");
    }
    if (!Array.isArray(probabilities)) {
        throw new TypeError("The second argument must be an array of numbers");
    }
    const randomArrayLength = findRandomArrayLength(probabilities);
    const normalizedProbabilities = probabilities.map(probability =>
        addZeros(probability, randomArrayLength)
    );
    const randomNumberArray = generateWeightedNumberArray(
        numberArray,
        normalizedProbabilities
    );
    const randomIndexPick = Math.floor(
        Math.random() * randomNumberArray.length
    );
    return randomNumberArray[randomIndexPick];
};

module.exports = {
    addZeros,
    findRandomArrayLength,
    generateWeightedNumberArray,
    generateWeightedRandomNumber
};
