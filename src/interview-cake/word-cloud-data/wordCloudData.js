/*
You want to build a word cloud, an infographic where the size of a word corresponds to how often it appears in the body of text.

To do this, you'll need data. Write code that takes a long string and builds its word cloud data in a dictionary ↴ , where the keys are words and the values are the number of times the words occurred.

Think about capitalized words.For example, look at these sentences:

'After beating the eggs, Dana read the next step:'
'Add milk and eggs, then add flour and sugar.'
What do we want to do with "After", "Dana", and "add" ? In this example, your final dictionary should include one "Add" or "add" with a value of 22. Make reasonable(not necessarily perfect) decisions about cases like "After" and "Dana".

Assume the input will only contain words and standard punctuation.
*/

const createWordCloud = (string) => {
    if (typeof string !== "string") {
        throw new TypeError(
            "The argument for createWordCloud must be of type string."
        );
    }

    if (!string.length) {
        return {};
    }

    const stringArray = splitWords(string);

    return stringArray.reduce((tracker, word) => {
        const newWord = word.toLowerCase();

        if (tracker[newWord]) {
            return { ...tracker, [newWord]: tracker[newWord] + 1 };
        } else {
            return { ...tracker, [newWord]: 1 };
        }
    }, {});
};

const splitWords = (string) => {
    if (typeof string !== "string") {
        throw new TypeError(
            "The argument for splitWords must be of type string."
        );
    }

    const words = [];

    if (!string.length) {
        return words;
    }

    let currentWordStartIndex = 0;
    let currentWordLength = 0;

    for (let i = 0; i < string.length; i++) {
        if (isAlphaChar(string[i])) {
            if (!currentWordLength) {
                currentWordStartIndex = i;
            }

            currentWordLength += 1;
        } else {
            if (currentWordLength) {
                words.push(
                    string.slice(
                        currentWordStartIndex,
                        currentWordStartIndex + currentWordLength
                    )
                );
            }
            currentWordLength = 0;
        }
    }

    return words;
};

const isAlphaChar = (char) => {
    if (typeof char !== "string") {
        throw new TypeError(
            "The argument for isAlphaChar must be of type string."
        );
    }

    return /[a-z]/.test(char.toLowerCase());
};

module.exports = { createWordCloud, splitWords, isAlphaChar };
