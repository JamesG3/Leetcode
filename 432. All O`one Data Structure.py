class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic_k_c = {}
        self.dic_c_k = {}
        self.max_key = -float('inf')
        self.min_key = float('inf')
        
    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
    
        self.dic_k_c[key] = self.dic_k_c.get(key, 0) + 1
        count = self.dic_k_c[key]
        self.dic_c_k[count] = self.dic_c_k.get(count, set())
        self.dic_c_k[count].add(key)
        
        self.max_key = max(self.max_key, count)
        prev = count - 1
        if prev == 0:
            self.min_key = min(self.min_key, count)
        else:
            # purge record
            if len(self.dic_c_k[prev]) == 1:
                del self.dic_c_k[prev]
            else:
                self.dic_c_k[prev].remove(key)
            
            if self.min_key not in self.dic_c_k:
                self.min_key = count
         
        
    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.dic_k_c:
            return
        
        cnt = self.dic_k_c[key]
        
        if cnt != 1:
            self.dic_c_k[cnt-1] = self.dic_c_k.get(cnt-1, set())
            self.dic_c_k[cnt-1].add(key)
            self.dic_k_c[key] = cnt-1
        else:
            del self.dic_k_c[key]
            
            
        if len(self.dic_c_k[cnt]) == 1:
            del self.dic_c_k[cnt]
        else:
            self.dic_c_k[cnt].remove(key)
        
        
        if self.min_key == 1:
            if self.min_key not in self.dic_c_k:
                if not self.dic_c_k:
                    self.min_key = float('inf')
                else:
                    self.min_key = sorted(self.dic_c_k.keys())[0]
        else:
            self.min_key = min(self.min_key, cnt-1)
            
        if self.max_key == 1:
            if self.max_key not in self.dic_c_k:
                self.max_key = -float('inf')
        else:
            if self.max_key not in self.dic_c_k:
                self.max_key = cnt - 1
        
            
    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        target = self.dic_c_k.get(self.max_key, set())
        return list(target)[0] if target else ''
        

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        target = self.dic_c_k.get(self.min_key, set())
        return list(target)[0] if target else ''
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()


'''
Implement a data structure supporting the following operations:

Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".
Challenge: Perform all these in O(1) time complexity.

Solution: Two hash tables (reverse hashtable)
Time: O(1) except self.min_key = sorted(self.dic_c_k.keys())[0] use O(nlogn)
'''
