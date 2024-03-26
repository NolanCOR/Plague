import importlib
import inspect
import os
import sys



class GeneratorLauncher():
    
    def __init__(self,lst_gen,lst_elem,output_path) -> None:
        self.lst_gen = lst_gen
        self.lst_elem = lst_elem
        self.output_path =output_path

    def generate(self):
        module_path = os.path.join(os.getcwd(),'generator')
        if not (module_path in sys.path):
            sys.path.append(module_path)


        print(sys.path)
        for gn in self.lst_gen:
            gn = gn[0:-3]
            self.handle_generator(gn)

        sys.path.remove(module_path)
        print(sys.path)
        
    
    def handle_generator(self,generator_name):
        try:
            print(f"{generator_name} \n")
            module_gen = importlib.import_module(generator_name)
            (first_class_name,first_class) = inspect.getmembers(module_gen, inspect.isclass)[1]
            print(inspect.getmembers(module_gen, inspect.isclass))
            print(type(first_class))
            instance_gen = first_class(self.lst_elem)
            print(instance_gen)
            getattr(instance_gen,"generate")(str(os.path.join(self.output_path,'pwd_list.txt')))
            print("end")
        except Exception as e:
            print(e)
        
        