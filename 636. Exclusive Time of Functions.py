class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = {}
        
        for log in logs:
            job, typ, time = log.split(':')
            job, time = int(job), int(time)
            if typ == 'start':
                if stack:
                    # if another job is added, calculate the time for job on the stack top
                    stack[-1][-1] += time - stack[-1][1]
                # [job id, prev start time, time sum]
                stack.append([job, time, 0])
            else:
                j, tm, cnt = stack.pop()
                res[job] = res.get(job, 0) + cnt + time - tm + 1
                # update the job on the stack top
                if stack:
                    stack[-1][1] = time + 1
                
        return [res[i] for i in range(len(res))]

'''
On a single threaded CPU, we execute some functions.  Each function has a unique id between 0 and N-1.

We store logs in timestamp order that describe when a function is entered or exited.

Each log is a string with this format: "{function_id}:{"start" | "end"}:{timestamp}".  For example, "0:start:3" means the function with id 0 started at the beginning of timestamp 3.  "1:end:2" means the function with id 1 ended at the end of timestamp 2.

A function's exclusive time is the number of units of time spent in this function.  Note that this does not include any recursive calls to child functions.

The CPU is single threaded which means that only one function is being executed at a given time unit.

Return the exclusive time of each function, sorted by their function id.

Solution: 
Time: O(n)
Space: O(n)

'''
