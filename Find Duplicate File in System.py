class Solution(object):
    def findDuplicate(self, paths):
        dic = {}
        for item in paths:
            path = item.split()
            rootpath = path[0]
            
            for file in path[1:]:
                tem = file.partition('(')       # extract the content and path
                name = tem[0]
                content = tem[-1][:-1]
                
                if content in dic:              # save root/path into dictionary
                    dic[content].append(rootpath+'/'+name)
                else:
                    dic[content] = [rootpath + '/' + name]
                    
        return [x for x in dic.values() if len(x)>1] 
                
                
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        
        # Input:
        # ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
        
        # Output:  
        # [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
