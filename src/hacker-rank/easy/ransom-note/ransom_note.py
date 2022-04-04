"""
Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting. He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use only whole words available in the magazine. He cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.

Example
magazine = "attack at dawn" 
note = "Attack at dawn"

The magazine has all the right words, but there is a case mismatch. The answer is No.

Function Description

Complete the checkMagazine function in the editor below. It must print Yes if the note can be formed using the magazine, or No.

checkMagazine has the following parameters:

- string magazine[m]: the words in the magazine
- string note[n]: the words in the ransom note

Prints

- string: either Yes or No, no return value is expected
"""

def check_magazine(magazine, note):
    """Takes in a magazine list and checks to see if ransom note list can be made from it"""
    if len(magazine) < len(note):
        print("No")
        return

    tracker = {}
    isNotePossible = False

    for i in range(len(magazine)):
        magazine_word = magazine[i]

        if not magazine_word in tracker:
            tracker[magazine_word] = 0

        tracker[magazine_word] += 1

    for i in range(len(note)):
        note_word = note[i]

        if not note_word in tracker:
            break
        else:
            tracker[note_word] -= 1

            if i == len(note) - 1:
                isNotePossible = True

    print("Yes" if isNotePossible else "No")