class File:

    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return True



with File('example.txt', 'a+') as file:
    file.write('Всем привет!')

