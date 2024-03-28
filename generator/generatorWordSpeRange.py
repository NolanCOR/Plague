from generator import Generator

class GeneratorWordSpeRange(Generator):
    def __init__(self, list) -> None:
        super().__init__(list)
        self.necessary = ['word','specialC','range']
        self.name = "GeneratorWordSpeRange"
        self.description = "this generator uses the following pattern : [word][specialC][number]"
        
    def generate(self,outputdir):
        
        def append_string_to_file(file_path, string_to_append):
            with open(file_path, 'a') as file:
                file.write(string_to_append)
        
        def string_password(word,int,sc):
            return f"{word.get()}{sc.get()}{int}\n"
        
        self.check_necessary()
        for word in self.words:
            for sc in self.specialC: 
                for range in self.ranges:  
                    for i in range.getRange():
                        append_string_to_file(outputdir,string_to_append=string_password(word,i,sc))
