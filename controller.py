class WordChecker:
    def __init__(self):
        pass

    def is_word(self, string):
        return ' ' not in string

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
    

class SpecialCharChecker:
    def __init__(self):
        pass

    def is_special_char(self, string):
        special_chars = set("@_!#$%^&*()<>?/+-|}{~:]£*µ§")
        return any(char in special_chars for char in string)
