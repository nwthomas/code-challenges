"""
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
"""

from typing import List

DELIMITER = "π"

def encode(strs: List[str]) -> str:
    result = ""
    lengths = ""
    concatted_strs = ""
    for new_str in strs:
        new_length = str(len(new_str))
        lengths += new_length + ","
        concatted_strs += new_str
    result += lengths + DELIMITER + concatted_strs
    return result

def decode(s: str) -> List[str]:
    result = []
    sizes = []
    i = 0
    while s[i] != DELIMITER:
        current_size = ""
        while s[i] != ",":
            current_size += s[i]
            i += 1
        sizes.append(int(current_size))
        i += 1
    i += 1
    for size in sizes:
        result.append(s[i:i+size])
        i += size
    return result
