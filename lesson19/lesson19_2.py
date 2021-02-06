import os
class FileManager:
    counter = 0

    @classmethod
    def get_countetr(cls):
        return cls.counter

    def __init__(self, filename, mode):
        if os.path.exists(filename):
            self.filename = filename
        if mode in [ 'r' , 'w', 'a' , 'x' , 'a+']:
            self.mode = mode
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        FileManager.counter += 1
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print(f' менеджер зкарыт уже {self.counter} раз ')
        self.file.close()

if __name__ == '__main__':
    pass

