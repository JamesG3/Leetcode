import hashlib

class Codec:
    
    def __init__(self):
        self.url = {}

    def encode(self, longUrl):
        H = hashlib.sha1(longUrl).hexdigest()
        
        self.url[H[:10]] = longUrl
        
        return 'http://tinyurl.com/'+H[:10]
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        

    def decode(self, shortUrl):
        
        return self.url[shortUrl[-10:]]
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


#TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.
