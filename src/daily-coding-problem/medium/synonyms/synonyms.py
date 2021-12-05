"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You are given a set of synonyms, such as (big, large) and (eat, consume). Using this set, determine if two sentences with the same number of words are equivalent.

For example, the following two sentences are equivalent:

"He wants to eat food."
"He wants to consume food."
Note that the synonyms (a, b) and (a, c) do not necessarily imply (b, c): consider the case of (coach, bus) and (coach, teacher).

Follow-up: what if we can assume that (a, b) and (a, c) do in fact imply (b, c)?
"""

def create_reference_dict(*args):
    """Util to take in a list of sets and returns a dictionary reference"""
    reference_dict = {}

    for arg in args:
        first_value, second_value = arg

        if first_value in reference_dict:
            reference_dict[first_value].append(second_value)
        else:
            reference_dict[first_value] = [second_value]

        if second_value in reference_dict:
            reference_dict[second_value].append(first_value)
        else:
            reference_dict[second_value] = [first_value]

    return reference_dict

def are_words_synonyms(reference_dict, first_word, second_word):
    """Takes in two words with a reference dictionary and checks if they're synonyms"""
    return True if second_word in reference_dict[first_word] else False

def are_sentences_equivalent(synonyms, first_word, second_word):
    """Takes in synonyms and two sentences and returns if the sentences are equivalent"""
    if len(first_word) != len(second_word):
        return False

    reference_dict = create_reference_dict(synonyms)

    first_word_list = first_word
    first_word_list.split()

    second_word_list = second_word
    second_word_list.split()

    for i in range(0, len(first_word_list)):
        if first_word_list[i] != second_word_list[1] and not are_words_synonyms(reference_dict, first_word, second_word):
            return False
    
    return True


