class Range:
    def __init__(self,start,end) -> None:
        self.start = start
        self.end = end
    
    def getRange(self):
        return range(self.start,self.end + 1)
    
    
class SpecialCase:
    def __init__(self,char) -> None:
        self.char = char
        
    def get(self):
        return self.char
    
class Word():
    def __init__(self,word) -> None:
        self.word = word
        
    def get(self):
        return self.word