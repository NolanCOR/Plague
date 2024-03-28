from generator import Generator

class GeneratorWordRangeSpe(Generator):
    def __init__(self, list, outputdir) -> None:
        super().__init__(list,outputdir=outputdir)
        self.necessary = ['word','specialC','range']
        self.name = "GeneratorWordRangeSpe"
        self.description = "this generator uses the following pattern : [word][number][specialC]"
        
    def generate(self):
        def string_password(word,int,sc):
            return f"{word.get()}{int}{sc.get()}\n"

        for word in self.words:
            for range in self.ranges:
                for i in range.getRange():
                    for sc in self.specialC:
                        self.generated.append(string_password(word,i,sc))
