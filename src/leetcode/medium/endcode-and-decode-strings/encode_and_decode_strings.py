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

ENCODING_SPACER = "|.del~|"

def encode(l: List[str]) -> str:
    global ENCODING_SPACER

    encodedString = ""

    for i, s in enumerate(l):
        encodedString += s if i == 0 else ENCODING_SPACER + s

    return encodedString


def decode(s: str) -> List[str]:
    return s.split(ENCODING_SPACER)