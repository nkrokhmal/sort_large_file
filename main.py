import argparse
from app import generate_file, SortFile


def parse_memory(string):
    if string[-1].lower() == 'k':
        return int(string[:-1]) * 1024
    elif string[-1].lower() == 'm':
        return int(string[:-1]) * 1024 * 1024
    elif string[-1].lower() == 'g':
        return int(string[:-1]) * 1024 * 1024 * 1024
    else:
        return int(string)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--row', help='Number of rows')
    parser.add_argument('--length', help='Length of string')
    parser.add_argument('--mem', help='Memory, default = 1g', default='1g')
    parser.add_argument('--newdata', help='Create new data?', default='True')

    args = parser.parse_args()
    if bool(args.newdata):
        print('Creating new file')
        generate_file(int(args.row), int(args.length))
    file_sorting = SortFile(row=int(args.row), memory=parse_memory(args.mem), line_length=int(args.length))
    print('Splitting original fata into small files')
    file_sorting.split_files()
    print('Merging files')
    file_sorting.merge_files()
    print('Deleting other files')
    file_sorting.delete_files()
    print('Sorting finished')