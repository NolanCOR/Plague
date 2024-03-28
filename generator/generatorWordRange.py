from generator import Generator

class GeneratorWordRange(Generator):
    def __init__(self,list,outputdir) -> None:
        super().__init__(list,outputdir=outputdir)
        self.necessary = ['word','range']
        self.name = "GeneratorWordRange"
        self.description = "this generator uses the following pattern : [word][number]"
        self.generated = []
        
    def generate(self):
        def string_password(word,int):
            return f"{word.get()}{int}\n"
        
        for word in self.words:
            for range in self.ranges:
                for i in range.getRange():
                    self.generated.append(string_password(word,i))
