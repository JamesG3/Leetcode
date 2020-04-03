class LFUCache:

    def __init__(self, capacity: int):
        self.dic = {}
        self.key_freq = {}
        self.freq_keys = {}
        self.capacity = capacity
        self.min_cnt = 1
    
    
    def increment(self, key):
        self.key_freq[key] = self.key_freq.get(key, 0) + 1
        cur_cnt = self.key_freq[key]
        self.freq_keys[cur_cnt] = self.freq_keys.get(cur_cnt, []) + [key]
        if cur_cnt > 1:
            self.freq_keys[cur_cnt-1].remove(key)
        
    def get(self, key: int) -> int:
        if key in self.dic:
            self.increment(key)
            return self.dic[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return -1
        
        if len(self.dic) < self.capacity:
            self.dic[key] = value
            self.increment(key)
        else:
            if key not in self.dic:
                while not self.freq_keys[self.min_cnt]:
                    self.min_cnt += 1
                rm_key = self.freq_keys[self.min_cnt].pop(0)
                del self.key_freq[rm_key]
                del self.dic[rm_key]
                self.put(key, value)
                self.min_cnt = 1
            
            else:
                self.dic[key] = value
                self.increment(key)
            
        
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

'''
Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Note that the number of times an item is used is the number of calls to the get and put functions for that item since it was inserted. This number is set to zero when the item is removed.

Follow up:
Could you do both operations in O(1) time complexity?

Solution: Three hash tables
Time: 
    put: O(1) - O(n)
    get: O(1)
'''
