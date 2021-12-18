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

def are_deeply_linked_synonyms(reference_dict, first_word, second_word):
    """Takes in two words with a reference dictionary and iteratively checks if the words (with any in between) are synonyms"""
    if first_word not in reference_dict or second_word not in reference_dict:
        return False

    tracker = {}
    stack = [word for word in reference_dict[first_word]]

    while len(stack) > 0:
        current_word = stack.pop()

        if current_word in tracker:
            continue
        else:
            tracker[current_word] = True

        current_word_synonyms = reference_dict[current_word]

        for word in current_word_synonyms:
            if word == second_word:
                return True
            elif word in tracker:
                continue
            else:
                stack.append(word)
                
    return False

def create_reference_dict(synonyms):
    """Util to take in a list of sets and returns a dictionary reference"""
    reference_dict = {}

    for word_set in synonyms:
        first_value, second_value = word_set

        if first_value in reference_dict:
            reference_dict[first_value].append(second_value)
        else:
            reference_dict[first_value] = [second_value]

        if second_value in reference_dict:
            reference_dict[second_value].append(first_value)
        else:
            reference_dict[second_value] = [first_value]

    return reference_dict

def are_sentences_equivalent(synonyms, first_str, second_str):
    """Takes in synonyms and two sentences and returns if the sentences are equivalent"""
    reference_dict = create_reference_dict(synonyms)
    first_str_list = first_str.split()
    second_str_list = second_str.split()

    if len(first_str_list) != len(second_str_list):
        return False

    for i in range(0, len(first_str_list)):
        if first_str_list[i] == second_str_list[i]:
            continue
        elif not are_deeply_linked_synonyms(reference_dict, first_str_list[i], second_str_list[i]):
            return False
    
    return True


