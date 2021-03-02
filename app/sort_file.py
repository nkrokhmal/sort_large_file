import os
from config import DATA_FOLDER, SORTED_DATA_PATH, DATA_PATH
from app.heap_sort import LinesHeap
from app.line_iterator import LineIterator


class ChunkLine:
    def __init__(self, line=None, line_iterator=None, filepath=None):
        self.line = line
        self.line_iterator = line_iterator
        self.filepath = filepath


class SortFile:
    def __init__(self,  line_length, row, memory):
        self.max_string = 'z' * (line_length + 1)
        self.data_folder = DATA_FOLDER
        self.file_sorted = open(SORTED_DATA_PATH, 'w')
        self.data_path = DATA_PATH

        self.memory = memory
        self.row = row

        self.chunk_items = []
        self.heap = LinesHeap()

    def save_list_of_strings(self, path, chunk):
        with open(path, 'w') as file:
            for item in chunk:
                file.write(f'{item}')

    def write_line(self, line):
        self.file_sorted.write(line)

    def find_chunk_size(self):
        return int(self.memory / 8 / len(self.max_string))

    def split_files(self):
        chunk_size = self.find_chunk_size()
        file_index = 0
        counter = 0
        chunk = []
        with open(self.data_path, 'r') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                chunk.append(line)
                counter += 1
                if counter == chunk_size:
                    chunk_filepath = os.path.join(self.data_folder, f'data_{file_index}.txt')
                    self.save_list_of_strings(chunk_filepath, sorted(chunk))
                    self.chunk_items.append(ChunkLine(line_iterator=LineIterator(chunk_filepath), filepath=chunk_filepath))
                    counter = 0
                    file_index += 1
                    chunk = []
        if chunk:
            chunk_filepath = os.path.join(self.data_folder, f'data_{file_index}.txt')
            self.save_list_of_strings(chunk_filepath, sorted(chunk))
            self.chunk_items.append(ChunkLine(line_iterator=LineIterator(chunk_filepath), filepath=chunk_filepath))

    def merge_files(self):
        chunks_first_lines = []
        for chunk_item in self.chunk_items:
            chunk_item.line = next(chunk_item.line_iterator)
            chunks_first_lines.append(chunk_item)

        chunks_length = len(chunks_first_lines)
        self.heap.build(chunks_first_lines)
        while True:
            if chunks_first_lines[0].line == self.max_string:
                break
            self.write_line(chunks_first_lines[0].line)
            chunks_first_lines[0].line = next(chunks_first_lines[0].line_iterator)
            if not chunks_first_lines[0].line:
                chunks_first_lines[0].line = self.max_string
            self.heap.heapify(chunks_first_lines, 0, chunks_length)

    def delete_files(self):
        for chunk in self.chunk_items:
            os.remove(chunk.filepath)