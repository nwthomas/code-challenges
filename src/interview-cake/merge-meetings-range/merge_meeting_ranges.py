"""
Your company built an in-house calendar tool called HiCal. You want to add a feature to see the times in a day when everyone is available.

To do this, you’ll need to know when any team is having a meeting. In HiCal, a meeting is stored as a tuple ↴ of integers (start_time, end_time). These integers represent the number of 30-minute blocks past 9:00am.

For example:

  (2, 3)  # Meeting from 10:00 – 10:30 am
(6, 9)  # Meeting from 12:00 – 1:30 pm

Python 3.6
Write a function merge_ranges() that takes a list of multiple meeting time ranges and returns a list of condensed ranges.

For example, given:

  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

Python 3.6
your function would return:

  [(0, 1), (3, 8), (9, 12)]

Do not assume the meetings are in order. The meeting times are coming from multiple teams.

Write a solution that's efficient even when we can't put a nice upper bound on the numbers representing our time ranges. Here we've simplified our times down to the number of 30-minute slots past 9:00 am. But we want the function to work even for very large numbers, like Unix timestamps. In any case, the spirit of the challenge is to merge meetings where start_time and end_time don't have an upper bound.
"""


def merge_meeting_ranges(meetings):
    """Calls merge sort on list of meetings and combines ranges"""
    if type(meetings) != list:
        raise TypeError(
            "The argument for merge_meeting_ranges must be of type list")
    if len(meetings) < 2:
        return meetings

    sorted_meetings = merge_sort(meetings)
    merged_meetings = [sorted_meetings[0]]

    # (0, 1), (3, 5)
    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        if current_meeting_start <= last_merged_meeting_end:
            merged_meetings[-1] = (last_merged_meeting_start,
                                   max(current_meeting_end, last_merged_meeting_end))
        else:
            merged_meetings.append(
                (current_meeting_start, current_meeting_end))

    return merged_meetings


def merge_sort(meetings):
    """Merge sorts a list"""

    if len(meetings) < 2:
        return meetings

    split_index = len(meetings) // 2

    left_side = merge_sort(meetings[:split_index])
    right_side = merge_sort(meetings[split_index:])

    return merge(left_side, right_side)


def merge(listA, listB):
    """Merges two lists together"""

    if len(listA) < 1:
        return listB
    if len(listB) < 1:
        return listA

    listA_index = 0
    listB_index = 0
    merged_list = []
    total_length = len(listA) + len(listB)

    while listA_index + listB_index < total_length:
        if len(listA) <= listA_index:
            merged_list.append(listB[listB_index])
            listB_index += 1
        elif len(listB) <= listB_index:
            merged_list.append(listA[listA_index])
            listA_index += 1
        elif listA[listA_index][0] < listB[listB_index][0]:
            merged_list.append(listA[listA_index])
            listA_index += 1
        else:
            merged_list.append(listB[listB_index])
            listB_index += 1

    return merged_list
