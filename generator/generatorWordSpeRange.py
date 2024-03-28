from generator import Generator

class GeneratorWordSpeRange(Generator):
    def __init__(self, list, outputdir) -> None:
        super().__init__(list,outputdir)
        self.necessary = ['word','specialC','range']
        self.name = "GeneratorWordSpeRange"
        self.description = "this generator uses the following pattern : [word][specialC][number]"
        
    def generate(self):
        def string_password(word,int,sc):
            return f"{word.get()}{sc.get()}{int}\n"
        
        for word in self.words:
            for sc in self.specialC: 
                for range in self.ranges:  
                    for i in range.getRange():
                        self.generated += string_password(word,i,sc)
