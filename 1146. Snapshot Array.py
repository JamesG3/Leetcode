class SnapshotArray:

    def __init__(self, length: int):
        self.array = {}
        self.snap_i = 0
        
    def set(self, index: int, val: int) -> None:
        if index not in self.array:
            self.array[index] = {'cur_val': None}
        self.array[index]['cur_val'] = val
            
        
    def snap(self) -> int:
        for k, v in self.array.items():
            self.array[k][self.snap_i] = v['cur_val']
        self.snap_i += 1
        return self.snap_i - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.array.get(index, {}).get(snap_id, 0)
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

'''
Implement a SnapshotArray that supports the following interface:
SnapshotArray(int length) initializes an array-like data structure with the given length.  Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id

Solution: Design Data Structure, Hasttable
Time, Space: O(n)
'''
