class SegTree(object):
    '''
    Segment Tree solution
    Time: Init-O(n), Update-O(lgn), RangeSum(lgn)
    '''
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.mid = (start + end) / 2
        self.sum = None
        self.left = None
        self.right = None
        
        
class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums:
            return None
        self.l = nums
        self.root = self._builder(0, len(nums) - 1)
        
        
    def _builder(self, start, end):
        node = SegTree(start, end)
        if start == end:
            node.sum = self.l[start]
        else:
            mid = (start + end) / 2
            node.left = self._builder(start, mid)
            node.right = self._builder(mid + 1, end)
            node.sum = node.left.sum + node.right.sum
        return node
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        print 'update'
        print i,val
        nodes = [self.root]
        node = nodes[-1]
        while not (node.start == node.end == i):
            if i <= node.mid:
                nodes.append(node.left)
                node = node.left
            else:
                nodes.append(node.right)
                node = node.right
        
        node = nodes.pop()
        node.sum = val
        
        while nodes:
            node = nodes.pop()
            node.sum = node.left.sum + node.right.sum
            
        
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """ 
        # recursive calculation
        def helper(node, s, e):
            if node.start == s and node.end == e:
                return node.sum
            
            # if entire range is on one side
            if node.mid < s:
                return helper(node.right, s, e)
            elif node.mid >= e:
                return helper(node.left, s, e)
            
            # if the range covers both left and right side
            else:
                return helper(node.left, s, node.mid) + helper(node.right, node.mid + 1, e)
            
        return helper(self.root, i, j)
                
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
