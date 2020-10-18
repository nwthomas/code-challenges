"""
I want to learn some big words so people think I'm smart.

I opened up a dictionary to a page in the middle and started flipping through, looking for words I didn't know. 
I put each word I didn't know at increasing indices in a huge list I created in memory. When I reached the end 
of the dictionary, I started from the beginning and did the same thing until I reached the page I started at.

Now I have a list of words that are mostly alphabetical, except they start somewhere in the middle of the
alphabet, reach the end, and then start from the beginning of the alphabet. In other words, this is an
alphabetically ordered list that has been "rotated." For example:

words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

Write a function for finding the index of the "rotation point," which is where I started working from the
beginning of the dictionary. This list is huge (there are lots of words I don't know) so we want to be
efficient here.
"""

"""
1. Start at start_index = 0, end_index = end of list
2. Pick the middle number
3. 
"""




from random import randrange
def find_rotation_point(word_list):
    """Takes in a list of words and finds the rotation point"""

    if type(word_list) != list:
        raise TypeError("The argument for word_list must be of type list.")
    elif len(word_list) <= 1:
        return word_list[0] if len(word_list) > 0 else None

    start_index = 0
    end_index = len(word_list) - 1

    while start_index < end_index:
        guess_index = start_index + ((end_index - start_index) // 2)

        if end_index - start_index > 2:
            if word_list[start_index] > word_list[guess_index]:
                end_index = guess_index
            else:
                start_index = guess_index
        else:
            first_word = word_list[start_index]
            second_word = word_list[end_index]
            return first_word if first_word < second_word else second_word
