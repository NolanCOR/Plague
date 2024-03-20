import models as m

class Generator:
    def __init__(self) -> None:
        self.ranges =[]
        self.specialC = []
        self.words = []
        
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

class GeneratorWordRange(Generator):
    def __init__(self, list) -> None:
        super().__init__(list)
        
    def generate(self,outputdir):
        
        def append_string_to_file(file_path, string_to_append):
            with open(file_path, 'a') as file:
                file.write(string_to_append)
        
        def string_password(word,int):
            return f"{word.get()}{int}\n"
        
        for word in self.words:
            for range in self.ranges:
                for i in range.getRange():
                    append_string_to_file(outputdir,string_to_append=string_password(word,i))
            

class GeneratorWordRangeSpe(Generator):
    def __init__(self, list) -> None:
        super().__init__(list)
        
    def generate(self,outputdir):
        
        def append_string_to_file(file_path, string_to_append):
            with open(file_path, 'a') as file:
                file.write(string_to_append)
        
        def string_password(word,int,sc):
            return f"{word.get()}{int}{sc.get()}\n"
        
        for word in self.words:
            for range in self.ranges:
                for i in range.getRange():
                    for sc in self.specialC:
                        append_string_to_file(outputdir,string_to_append=string_password(word,i,sc))
                        
class GeneratorWordSpeRange(Generator):
    def __init__(self, list) -> None:
        super().__init__(list)
        
    def generate(self,outputdir):
        
        def append_string_to_file(file_path, string_to_append):
            with open(file_path, 'a') as file:
                file.write(string_to_append)
        
        def string_password(word,int,sc):
            return f"{word.get()}{sc.get()}{int}\n"
        
        for word in self.words:
            for range in self.ranges:
                for i in range.getRange():
                    for sc in self.specialC:
                        append_string_to_file(outputdir,string_to_append=string_password(word,i,sc))