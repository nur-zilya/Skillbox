class File:

    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.name, self.mode)
        if not self.file:
            self.file = open(self.name, 'a+')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            pass
        self.file.close()
        return True



with File('example1.txt', 'w') as file:
    file.write('Всем привет!')

