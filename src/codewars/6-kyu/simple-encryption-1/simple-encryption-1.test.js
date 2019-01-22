const { encrypt, decrypt } = require("./simple-encryption-1");

// Encrypting Function
test("Encrypts string by taking every second character, makinga new string, and concatentating them", () => {
  expect(encrypt("This is a test!", 1)).toBe("hsi  etTi sats!");
  expect(encrypt("This is a test!", 2)).toBe("s eT ashi tist!");
});

// Decrypting Function
test("Decrypts string by taking second half of string and injecting each letter from the beginning every 2 characters", () => {
  expect(decrypt("s eT ashi tist!", 2)).toBe("This is a test!");
  expect(decrypt("hsi  etTi sats!", 1)).toBe("This is a test!");
});
