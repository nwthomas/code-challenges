/*

https://www.codewars.com/kata/57814d79a56c88e3e0000786

For building the encrypted string:
Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
Do this n times!

Examples:
"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"

Write two methods:
function encrypt(text, n)
function decrypt(encryptedText, n)

For both methods:
If the input-string is null or empty return exactly this value!
If n is <= 0 then return the input text.

*/

function encrypt(text: string | null, n: number) {
    if (text === null) return null;
    if (text === "") return "";
    if (n <= 0) return text;
    while (n > 0) {
        const textArr: string[] = text!.split("");
        var evenArr = textArr.filter((letter, index) => (index + 1) % 2 === 0);
        var oddArr: string[] = textArr.filter(
            (letter, index) => (index + 1) % 2 !== 0,
        );
        n--;
        text = evenArr.join("") + oddArr.join("");
    }
    return text;
}

function decrypt(encryptedText: string | null, n: number) {
    if (encryptedText === null) return null;
    if (encryptedText === "") return "";
    if (n <= 0) return encryptedText;
    while (n > 0) {
        n--;
        const textArr: string[] = encryptedText.split("");
        var evenArr = textArr.slice();
        var oddArr: string[] = evenArr.splice(
            Math.floor(encryptedText.length / 2),
        );
        let tempStr = [];

        for (let i = 0; i < encryptedText.length; i++) {
            if (i % 2 === 0) {
                let tempOdd = oddArr.shift();
                tempStr.push(tempOdd);
            } else {
                let tempEven = evenArr.shift();
                tempStr.push(tempEven);
            }
        }
        encryptedText = tempStr.join("");
    }
    return encryptedText;
}

export { encrypt, decrypt };
