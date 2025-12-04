/*
https://leetcode.com/problems/encode-and-decode-strings/description

Description
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Wechat reply 【Google】 get the latest requent Interview questions. (wechat id : jiuzhang0607)

Example 1:
Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"

Example 2:
Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"
*/

const DELIMITER = "##BREAK##";

const encode = (strs) => {
    let nums = "";
    let concattedStr = "";
    for (let i = 0; i < strs.length; i++) {
        const str = strs[i];
        nums += `${str.length}`;
        if (i < strs.length - 1) {
            nums += ",";
        }
        concattedStr += str;
    }

    return nums + DELIMITER + concattedStr;
};

const decode = (str) => {
    const [nums, strs] = str.split(DELIMITER);
    const result = [];

    const numsArr = nums.split(",");
    let strIndex = 0;
    for (let i = 0; i < numsArr.length; i++) {
        const num = parseInt(numsArr[i], 10);
        if (!isNaN(num)) {
            result.push(strs.substring(strIndex, strIndex + num));
            strIndex += num;
        }
    }

    return result;
};

module.exports = { encode, decode, DELIMITER };
