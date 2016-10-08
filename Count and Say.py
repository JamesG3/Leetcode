class Solution(object):
    def countAndSay(self, n):
        res=['1']
        if n == 0 or n == 1:
            return res[-1]
        while n!=1:
            tem=''
            count=1
            last=res[-1]
            for m in range(0,len(last)):
                if m != len(last)-1:
                    if last[m]==last[m+1]:
                        count+=1
                    else:
                        tem+="%s"%count
                        tem+="%s"%last[m]
                        count=1
                else:
                    if last[m] == last[m-1]:
                        tem+="%s"%count
                        tem+="%s"%last[m]
                        count=1
                    else:
                        count=1
                        tem+="%s"%count
                        tem+="%s"%last[m]
            res.append(tem)
            n-=1
            
        return res[-1]
            
        
        """
        :type n: int
        :rtype: str
        """
        
