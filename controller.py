class WordChecker:
    def __init__(self):
        pass

    def is_word(self, string):
        return ' ' not in string
    
    def check(self,string):
        if string is not None:
            if(self.is_word(string)):
                return True
        return False

class IntRangeChecker:
    def __init__(self):
        pass

    def is_int_range(self, string):
        if not string.startswith('[') or not string.endswith(']'):
            return False
        ints = string[1:-1].split('...')
        if len(ints) != 2:
            return False
        try:
            start, end = map(int, ints)
            return start <= end
        except ValueError:
            return False
    
    def check(self,string):
        if string is not None:
            if(self.is_int_range(string)):
                return True
        return False
    

class SpecialCharChecker:
    def __init__(self):
        pass

    def is_special_char(self, string):
        special_chars = set("@_!#$%^&*()<>?/+-|}{~:]£*µ§")
        return len(string) == 1 and (string in special_chars)

    def check(self,string):
        if string is not None:
            if(self.is_special_char(string)):
                return True
        return False