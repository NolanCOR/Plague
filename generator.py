import models as m

class Generator:
    def __init__(self) -> None:
        self.ranges =[]
        self.specialC = []
        self.words = []
        self.necessary = []
        self.name = "Default Generator Name"
        self.description = "Default Generator Description"
        
    def __init__(self,list) -> None:
        self.ranges =[]
        self.specialC = []
        self.words = []
        self.add(listToCheck=list)
        
    def add(self,listToCheck):
        for e in listToCheck:
            if (type(e) == m.Range):
                self.ranges.append(e)
            elif (type(e) == m.SpecialCase):
                self.specialC.append(e)
            elif (type(e) == m.Word):
                self.words.append(e)
            else:
                raise Exception(f"{e} should not be added to generator")
            
    def not_empty(self, *args):
        for arg in args:
            if len(arg = 0):
                return False
        return True

    def check_necessary(self):
        if ("range" in self.necessary and len(self.ranges) == 0):
            raise Exception("These should be range in this generator")
        if ("word" in self.necessary and len(self.words) == 0):
            raise Exception("These should be words in this generator")
        if ("specialC" in self.necessary and len(self.specialC) == 0):
            raise Exception("These should be special characters in this generator")    
    