const { WordDictionary } = require("./designAddAndSearchWordsDataStructure");

describe("WordDictionary", () => {
    it("instantiates a new version of the WordDictionary class", () => {
        const wordDictionary = new WordDictionary();
        expect(wordDictionary instanceof WordDictionary).toBe(true);
    });

    it("adds and can search a word to the word dictionary", () => {
        const wordDictionary = new WordDictionary();
        wordDictionary.addWord("test");
        expect(wordDictionary.search("test")).toBe(true);
    });

    it("returns false if a word is not found in the word dictionary", () => {
        const wordDictionary = new WordDictionary();
        wordDictionary.addWord("test");
        expect(wordDictionary.search("tesy")).toBe(false);
    });

    it("returns true if a word is found in the word dictionary using a dot", () => {
        const wordDictionary = new WordDictionary();
        wordDictionary.addWord("test");
        expect(wordDictionary.search("t.st")).toBe(true);
    });

    it("returns true if a word is found in the word dictionary using multiple dots", () => {
        const wordDictionary = new WordDictionary();
        wordDictionary.addWord("test");
        expect(wordDictionary.search("t..t")).toBe(true);
    });

    it("returns false if the word is not found in the word dictionary using a dot", () => {
        const wordDictionary = new WordDictionary();
        wordDictionary.addWord("test");
        expect(wordDictionary.search("..ss")).toBe(false);
    });

    it("returns false if the word is not found in the word dictionary using multiple dots longer than word length", () => {
        const wordDictionary = new WordDictionary();
        wordDictionary.addWord("test");
        expect(wordDictionary.search("tes..")).toBe(false);
    });
});
