class LineIterator:
    def __init__(self, file_path):
        self.file = open(file_path)

    def __iter__(self):
        return self

    def __next__(self):
        return self.file.readline()

