#----------------Solution 1 : BFS level traversal-----------
''' Time Complexity : O(n) 
    Space Complexity : O(n) 
    Did this code successfully run on Leetcode : Yes
    Any problem you faced while coding this :  No

   Approach : Maintain the size of queue. After traversing one level add the list to result
'''
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        q = []
        q.append(root)
        while q:
            size = len(q)
            l = []
            for i in range(size):
                node = q.pop(0)
                l.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(l)
        
        return result

#----------------Solution 1 : DFS traversal-----------
''' Time Complexity : O(n) 
    Space Complexity : O(h) 
    Did this code successfully run on Leetcode : Yes
    Any problem you faced while coding this :  No

   Approach : Maintain global result, when new level is encountered create new list at the index of level.
              Traverse the tree in preorder and append the nodes at respective index list.
'''
class Solution:
    def __init__(self):
        self.result = []
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        def dfs(root,level):
            if root is None:
                return 
            if len(self.result) == level:
                self.result.append([])
            
            self.result[level].append(root.val)
            dfs(root.left,level+1)
            dfs(root.right,level+1)
        
        dfs(root, 0)
        return self.result