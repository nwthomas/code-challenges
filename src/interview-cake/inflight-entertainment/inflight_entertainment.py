""""
You've built an inflight entertainment system with on-demand movie streaming.

Users on longer flights like to start a second movie right when their first one ends, but they complain that the plane usually lands before they can see the ending. So you're building a feature for choosing two movies whose total runtimes will equal the exact flight length.

Write a function that takes an integer flight_length (in minutes) and a list of integers movie_lengths (in minutes) and returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length.

When building your function:

Assume your users will watch exactly two movies
Don't make your users watch the same movie twice
Optimize for runtime over memory
"""


def find_exact_flight_movie_runtime(flight_length, movie_lengths):
    """Finds the exact combination of movie lengths to match a flight length if possible"""

    if type(flight_length) != int:
        raise TypeError(
            "The first argument of find_exact_flight_movie_runtime must be of type int.")

    if type(movie_lengths) != list:
        raise TypeError(
            "The second argument of find_exact_flight_movie_runtime must be of type list.")

    if len(movie_lengths) < 1 or flight_length < 0:
        return False

    prev_lengths = set()

    for length in movie_lengths:
        missing_length = flight_length - length

        if missing_length in prev_lengths:
            return True
        else:
            prev_lengths.add(length)

    return False
