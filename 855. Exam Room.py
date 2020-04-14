class ExamRoom:

    def __init__(self, N: int):
        self.seats = []
        self.N = N
    
    def seat(self) -> int:
        if not self.seats:
            position = 0
        else:
            position, cur_dis = 0, self.seats[0]
            for i, seat in enumerate(self.seats):
                if i == 0:
                    continue
                
                prev = self.seats[i-1]
                # calculate the estimated distance for the new student, notice that distance of 010 == distance of 0100, need to select the most left one in such cases
                tmp_dis = (seat - prev)//2
                
                if tmp_dis > cur_dis:
                    cur_dis = tmp_dis
                    position = cur_dis + prev
                    
            right_d = self.N - 1 - self.seats[-1]
            # sit on the right most seat
            if right_d > cur_dis:
                cur_dis = right_d
                position = self.N - 1
            
        bisect.insort(self.seats, position)
        return position


    def leave(self, p: int) -> None:
        self.seats.remove(p)
        

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)


'''
In an exam room, there are N seats in a single row, numbered 0, 1, 2, ..., N-1.

When a student enters the room, they must sit in the seat that maximizes the distance to the closest person.  If there are multiple such seats, they sit in the seat with the lowest number.  (Also, if no one is in the room, then the student sits at seat number 0.)

Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat() returning an int representing what seat the student sat in, and ExamRoom.leave(int p) representing that the student in seat number p now leaves the room.  It is guaranteed that any calls to ExamRoom.leave(p) have a student sitting in seat p.

Solution: Binary search, bisect.insort method, sort, greedy
Time: O(n), where n is the number of current students
Space: O(n)
'''
