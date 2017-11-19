"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        dic = {}
        global ivalue
        ivalue = 0
        Length = len(employees)
        
        for i in xrange(Length):        # hashtable
            dic[employees[i].id] = [employees[i].importance, employees[i].subordinates]
        
        def helper(id):                 # dfs
            global ivalue
            ivalue += dic[id][0]
            if dic[id][-1]:
                for ID in dic[id][-1]:
                    helper(ID)
            return 
        
        helper(id)
        
        return ivalue
    
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        
        # given a data structure of employee information (a list of objects), which includes the employee's unique id, his importance value and his direct subordinates' id.
        # return the sum of importance value from all direct and non-direct subordinates.
        
