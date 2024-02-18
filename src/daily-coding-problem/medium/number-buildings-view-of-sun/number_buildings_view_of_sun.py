"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Mailchimp.

You are given an array representing the heights of neighboring buildings on a city street, from east to west. The city assessor would like you to write an algorithm that returns how many of these buildings have a view of the setting sun, in order to properly value the street.

For example, given the array [3, 7, 8, 3, 6, 1], you should return 3, since the top floors of the buildings with heights 8, 6, and 1 all have an unobstructed view to the west.

Can you do this using just one forward pass through the array?
"""

from typing import List

def find_number_buildings_view_of_sun(building_heights: List[int]) -> int:
    buildings_with_view_totals = 0
    current_max_height = 0

    for i in range(len(building_heights) - 1, -1, -1):
        current_height = building_heights[i]

        if current_height > current_max_height:
            current_max_height = current_height
            buildings_with_view_totals += 1

    return buildings_with_view_totals

