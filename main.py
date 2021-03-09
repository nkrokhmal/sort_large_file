import argparse
from app import generate_file, SortFile
from config import TMP_DATA_FOLDER
import os
import shutil


def parse_memory(string):
    if string[-1].lower() == 'k':
        return int(string[:-1]) * 1024
    elif string[-1].lower() == 'm':
        return int(string[:-1]) * 1024 * 1024
    elif string[-1].lower() == 'g':
        return int(string[:-1]) * 1024 * 1024 * 1024
    else:
        return int(string)


def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def delete_tmp_folder():
    for filename in os.listdir(TMP_DATA_FOLDER):
        file_path = os.path.join(TMP_DATA_FOLDER, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--row', help='Number of rows', default=100)
    parser.add_argument('--max_length', help='Length of string', default=100)
    parser.add_argument('--memory', help='Memory, default = 1g', default='1g')
    parser.add_argument('--new_data', help='Create new data?', default='True')

    args = parser.parse_args()
    try:
        if str2bool(args.new_data):
            print('Creating new file')
            generate_file(int(args.row), int(args.max_length))
        file_sorting = SortFile(row=int(args.row), memory=parse_memory(args.memory), line_length=int(args.max_length))
        print('---Splitting original fata into small files---')
        file_sorting.split_files()
        print('---Merging files---')
        file_sorting.merge_files()
        print('---Deleting other files---')
        file_sorting.delete_files()
        print('---Sorting finished---')
    except Exception as e:
        print(f'Exception occurred {e}')
        delete_tmp_folder()
