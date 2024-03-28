import os
import inspect


def inspecting(dir_path):
    result = []

    def iterate_python_files(directory):
        for (index,filename) in enumerate (os.listdir(directory)):
            if filename.endswith(".py"):
                with open(os.path.join(directory, filename), 'r') as file:
                    code = file.read()
                    code = code.split("\n")
                    description = None
                    name = None
                    for ligne in code:
                        if "self.description" in ligne:
                            ligne = ligne.split(" ")
                            for i in range(len(ligne)):
                                if ligne[i] == "self.description":
                                    description = ligne[i+2:]
                                    description = (' '.join(description))[1:-1]
                                    
                        if "self.name" in ligne:
                            ligne = ligne.split(" ")
                            for i in range(len(ligne)):
                                if ligne[i] == "self.name":
                                   name = ligne[i+2][1:-1]
                result.append((name,description,index,filename))
    iterate_python_files(dir_path)
    return result

