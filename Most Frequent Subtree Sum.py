# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        global dic
        dic = {}
        self.helper(root)
        
        freq = 0
        for n in dic:                   #find the max frequency
            freq = max(dic[n],freq)
            
        ans = []
        for n in dic:                   #append all sums with the highest frequency into ans
           if dic[n] == freq:
               ans.append(n)
        return ans
        
        
    def helper(self, root):             #calculate the sum of each subtree recursively, return the sum of current subtree
        global dic
        if root == None:
            return 0
        else:
            left = self.helper(root.left)
            right = self.helper(root.right)
            
            sum = left+right+root.val
            if sum in dic:              #count the frequency of every sum
                dic[sum] += 1
            else:
                dic[sum] = 1
                
            return sum
        
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        
        #Given the root of a tree, you are asked to find the most frequent subtree sum. 
        #The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). 
        #So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

