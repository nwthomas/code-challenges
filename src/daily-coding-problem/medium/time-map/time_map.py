"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Write a map implementation with a get function that lets you retrieve the value of a key at a particular time.

It should contain the following methods:

set(key, value, time): sets key to value for t = time.
get(key, time): gets the key at t = time.
The map should work like this. If we set a key at a particular time, it will maintain that value forever or until it gets set at a later time. In other words, when we get a key at a time, it should return the value that was set for that key set at the most recent time.

Consider the following examples:

d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 2) # set key 1 to value 2 at time 2
d.get(1, 1) # get key 1 at time 1 should be 1
d.get(1, 3) # get key 1 at time 3 should be 2
d.set(1, 1, 5) # set key 1 to value 1 at time 5
d.get(1, 0) # get key 1 at time 0 should be null
d.get(1, 10) # get key 1 at time 10 should be 1
d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 0) # set key 1 to value 2 at time 0
d.get(1, 0) # get key 1 at time 0 should be 2
"""


class TimeMap:
    def __init__(self):
        self._map = {}

    def set(self, key, value, time):
        """
        Sets a new key-value pair in self.map with a corresponding time value
        """
        if type(time) is not type(1):
            return TypeError("The time value must be an integer")
        self._map[key] = {"_value": value, "_time": time}

    def get(self, key, time):
        """
        Gets the value of a key if the time is greater-than-or-equal-to the
        set time, else it returns None
        """
        if key in self._map:
            info = self._map[key]
            return info["_value"] if info["_time"] <= time else None
        else:
            None

    def delete(self, key):
        """
        Deletes a key-value pair from self._map
        """
        del self._map[key]

    def values(self):
        """
        Returns all current mapped values in self._map
        """
        return self._map
