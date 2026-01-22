#----------------Solution 1 : BFS -----------
''' Time Complexity : O(V + E) 
    Space Complexity : O(V + E) 
    Did this code successfully run on Leetcode : Yes
    Any problem you faced while coding this :  No

   Approach : Using topological sort algorithm
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = defaultdict(list)
        count = 0
        indegree = [0 for _ in range(numCourses)]
        for crs,pre in prerequisites:
            hashmap[pre].append(crs)
            indegree[crs] += 1 
        q = []
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                count += 1
        while q:
            crs = q.pop(0)
            for pre in hashmap[crs]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    q.append(pre)
                    count += 1

        if count == numCourses:
            return True
        else:
            return False

#----------------Solution 2 : DFS -----------
''' Time Complexity : O(V + E) 
    Space Complexity : O(V + E) 
    Did this code successfully run on Leetcode : Yes
    Any problem you faced while coding this :  No

   Approach : Maintaining visited set to detect cycle, Travresing each node by dfs
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            hashmap[pre].append(crs)

        visited = set()
        def dfs(crs):
            #if no prerequisite return True
            if hashmap[crs] == []:
                return True
            if crs in visited:
                return False
            visited.add(crs)
            for pre in hashmap[crs]:
                if not dfs(pre):
                    return False
            #if True for all prereq remove from visited
            visited.remove(crs)
            # Dont traverse completed crs again
            hashmap[crs] = []
            return True
        #call dfs for all courses
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True