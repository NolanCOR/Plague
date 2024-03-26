from generator import Generator

class GeneratorWordRangeSpe(Generator):
    def __init__(self, list) -> None:
        super().__init__(list)
        self.necessary = ['word','specialC','range']
        self.name = "GeneratorWordRangeSpe"
        self.description = "test2"
        
    def generate(self,outputdir):
        
        def append_string_to_file(file_path, string_to_append):
            with open(file_path, 'a') as file:
                file.write(string_to_append)

        def string_password(word,int,sc):
            return f"{word.get()}{int}{sc.get()}\n"

        self.check_necessary()
        for word in self.words:
            for range in self.ranges:
                for i in range.getRange():
                    for sc in self.specialC:
                        append_string_to_file(outputdir,string_to_append=string_password(word,i,sc))
