class Solution(object):
    def canConstruct(self, text, source):
        
        text=list(text)
        source = list(source)
        
        for t in text:
            if t in source:
                #print(t)
                #print(source.index(t))
                source.pop(source.index(t))
                
            else:
                return False
            
        return True
                
        
        