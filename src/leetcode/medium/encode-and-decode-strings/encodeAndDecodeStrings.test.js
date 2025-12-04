const { encode, decode, DELIMITER } = require("./encodeAndDecodeStrings");

describe("encodeAndDecodeStrings", () => {
    describe("encode", () => {
        it("encodes a string correctly", () => {
            const result = encode(["this", "is", "a", "test"]);
            expect(result).toBe("4,2,1,4" + DELIMITER + "thisisatest");
        });
    });

    describe("decode", () => {
        it("decodes a string correctly", () => {
            const result = decode("4,2,1,4," + DELIMITER + "thisisatest");
            expect(result).toEqual(["this", "is", "a", "test"]);
        });
    });
});
