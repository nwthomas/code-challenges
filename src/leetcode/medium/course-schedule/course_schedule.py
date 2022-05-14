"""
https://leetcode.com/problems/course-schedule/submissions/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""

from typing import List

def can_finish_courses(numCourses: int, prerequisites: List[List[int]]) -> bool:
    preMap = { i: [] for i in range(0, numCourses) }
    
    for course, prereq in prerequisites:
        preMap[course].append(prereq)
        
    visited_set = set()
    
    def dfs_courses(course):
        if course in visited_set:
            return False
        if len(preMap[course]) == 0:
            return True
        
        visited_set.add(course)
        
        for prereq in preMap[course]:
            result = dfs_courses(prereq)
            
            if not result:
                return False
            
        preMap[course] = []
        
        visited_set.remove(course)
            
        return True
    
    for course in range(numCourses):
        result = dfs_courses(course)
        
        if not result:
            return False
        
    return True