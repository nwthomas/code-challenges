"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

A classroom consists of N students, whose friendships can be represented in an adjacency list. For example, the following descibes a situation where 0 is friends with 1 and 2, 3 is friends with 6, and so on.

{0: [1, 2],
 1: [0, 5],
 2: [0],
 3: [6],
 4: [],
 5: [1],
 6: [3]} 
Each student can be placed in a friend group, which can be defined as the transitive closure of that student's friendship relations. In other words, this is the smallest set such that no student in the group has any friends outside this group. 

For the example above, the friend groups would be {0, 1, 2, 5}, {3, 6}, {4}.

Given a friendship list such as the one above, determine the number of friend groups in the class.
"""

def find_friend_groups(adj_list):
    """Takes in an adjacency list and returns the number of friend groups"""
    groups_to_friends = {}
    friend_to_group = {}

    for person in adj_list:
        friends = adj_list[person]
        person_has_been_grouped = False

        # If the person has no friends, add them to a new group and skip all other logic
        if len(friends) == 0:
            new_group = len(groups_to_friends)
            groups_to_friends[new_group] = {person}
            friend_to_group[person] = new_group
            continue

        for friend in friends:
            # Person has not been grouped yet and friend hasn't either
            if person not in friend_to_group and friend not in friend_to_group:
                new_group = len(groups_to_friends)
                friend_to_group[friend] = new_group
                friend_to_group[person] = new_group
                groups_to_friends[new_group] = {person, friend}

            # Person has not been grouped yet and friend has
            elif person not in friend_to_group and friend in friend_to_group:
                group = friend_to_group[friend]
                friend_to_group[person] = group
                groups_to_friends[group].append(person)

            # Person has been grouped bug friend has not
            elif person in friend_to_group and friend not in friend_to_group:
                group = friend_to_group[person]
                friend_to_group[friend] = group
                groups_to_friends[group].add(friend)
            
            # Person and friend are in different groups already
            elif person in friend_to_group and friend in friend_to_group and friend_to_group[person] != friend_to_group[friend]:

                # Colocate to person's group
                friend_current_group = friend_to_group[friend]
                final_group = friend_to_group[person]
                final_friends_set = groups_to_friends[friend_current_group].add(groups_to_friends[final_group])
                groups_to_friends[final_group] = final_friends_set

                for friend in final_friends_set:
                    friend_to_group[friend] = final_group

                # Delete old friend's group from trackers
                del groups_to_friends[friend_current_group]

    # Return the length of properties in the groups_to_friends tracker which is the total number of groups
    return len(groups_to_friends)