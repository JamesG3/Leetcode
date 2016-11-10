class Solution(object):
    def originalDigits(self, s):
        dic={}
        for n in s:
            dic[n] = dic.get(n, 0) + 1
            
        res = []
        if "z" in dic and dic["z"]!=0:
            res += dic['z'] * "0"
            dic['e'] -= dic['z']
            dic['r'] -= dic['z']
            dic['o'] -= dic['z']
            dic['z'] = 0
        if "w" in dic and dic["w"]!=0:
            res += dic['w'] * "2"
            dic['t'] -= dic['w']
            dic['o'] -= dic['w']
            dic['w'] = 0
        if "x" in dic and dic["x"]!=0:
            res += dic['x'] * "6"
            dic['s'] -= dic['x']
            dic['i'] -= dic['x']
            dic['x'] = 0
        if "s" in dic and dic["s"]!=0:
            res += dic['s'] * "7"
            dic['e'] -= 2*dic['s']
            dic['v'] -= dic['s']
            dic['n'] -= dic['s']
            dic['s'] = 0
        if "v" in dic and dic["v"]!=0:
            res += dic['v'] * "5"
            dic['f'] -= dic['v']
            dic['i'] -= dic['v']
            dic['e'] -= dic['v']
            dic['v'] = 0
        if "f" in dic and dic["f"]!=0:
            res += dic['f'] * "4"
            dic['o'] -= dic['f']
            dic['u'] -= dic['f']
            dic['r'] -= dic['f']
            dic['f'] = 0
        if "o" in dic and dic["o"]!=0:
            res += dic['o'] * "1"
            dic['n'] -= dic['o']
            dic['e'] -= dic['o']
            dic['o'] = 0
        if "r" in dic and dic["r"]!=0:
            res += dic['r'] * "3"
            dic['t'] -= dic['r']
            dic['h'] -= dic['r']
            dic['e'] -= 2*dic['r']
            dic['r'] = 0
        if "t" in dic and dic["t"]!=0:
            res += dic['t'] * "8"
            dic['i'] -= dic['t']
            dic['g'] -= dic['t']
            dic['h'] -= dic['t']
            dic['e'] -= dic['t']
            dic['t'] = 0
        if "i" in dic and dic["i"]!=0:
            res += dic['i'] * "9"

        ans=""
        for n in sorted(res):
            ans+=n
        return ans
        
        
        """
        Given a non-empty string containing an out-of-order English representation of digits 0-9, 
        output the digits in ascending order.
        :type s: str
        :rtype: str
        
        zero    z 1
        one     o 7
        two     w 2
        three   r 8
        four    f 6
        five    v 5
        six     x 3
        seven   s 4
        eight   e 9
        nine   n 10
        
        Using unique mark for every number, delete corresponding letters in the dictionary,
        then find out the next unique mark.
        """
