"""
You created a game that is more popular than Angry Birds.

Each round, players receive a score between 0 and 100, which you use to rank them from highest to lowest. So far you're using an algorithm that sorts in O(n\lg{n})O(nlgn) time, but players are complaining that their rankings aren't updated fast enough. You need a faster sorting algorithm.

Write a function that takes:

a list of unsorted_scores
the highest_possible_score in the game
and returns a sorted list of scores in less than O(n\lg{n})O(nlgn) time.

For example:

unsorted_scores = [37, 89, 41, 65, 91, 53]
HIGHEST_POSSIBLE_SCORE = 100

# Returns [91, 89, 65, 53, 41, 37]
sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)

We’re defining n as the number of unsorted_scores because we’re expecting the number of players to keep climbing.

And, we'll treat highest_possible_score as a constant instead of factoring it into our big O time and space costs because the highest possible score isn’t going to change. Even if we do redesign the game a little, the scores will stay around the same order of magnitude.
"""


def sort_player_scores(unsorted_scores, highest_possible_score):
    """Takes in a list of unsorted scores and the highest possible scores and returns a list of sorted scores"""
    tracker = {}
    sorted_scores = []

    if type(unsorted_scores) != list:
        raise TypeError(
            "The first argument for sort_player_scores must be of type list.")
    elif type(highest_possible_score) != int:
        raise TypeError(
            "The second argument for sort_player_scores must be of type int.")
    elif len(unsorted_scores) < 1:
        return sorted_scores

    for score in unsorted_scores:
        if score in tracker:
            tracker[score] += 1
        else:
            tracker[score] = 1

    for i in range(highest_possible_score, -1, -1):
        if i in tracker:
            sorted_scores += [i] * tracker[i]

    return sorted_scores
