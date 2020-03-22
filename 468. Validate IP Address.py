import re

class Solution:
    def validIPAddress(self, IP: str) -> str:
        def if_ipv4(ipstr):
            parts = ipstr.split('.')
            if not len(parts) == 4:
                return False
            for part in parts:
                if part.startswith('0') and len(part) > 1:
                    return False
                
                for c in part:
                    if c not in '0123456789':
                        return False
                try:
                    if not 0 <= int(part) < 256:
                        return False
                except:
                    return False
            return True
            
        def if_ipv6(ipstr):
            parts = ipstr.split(':')
            if not len(parts) == 8:
                return False
            for part in parts:
                if len(part) > 4 or len(part) < 1:
                    return False
                
                for c in part:
                    if not c.lower() in '0123456789abcdef':
                        return False
            return True
        
        if if_ipv4(IP):
            return 'IPv4'
        elif if_ipv6(IP):
            return 'IPv6'
        else:
            return 'Neither'
        
'''
Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

Solution: Edge case, simulation, rule
Time: O(n)
Space: O(1)
'''
