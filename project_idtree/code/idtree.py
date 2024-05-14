''' 사용 예시

# 파일 단위 트리를 2단계 깊이까지 txt 파일로 내보내기
python idtree.py D:\AILAB -f -o ./result_dir.txt -l 2


# 폴더 단위 트리를 2단계 깊이까지 txt 파일로 내보내기
python idtree.py D:\AILAB -d -o ./result_dir.txt -l 2


'''

import os
import argparse
import time
print("Welcome to Inventis Data Tree")
print("Loading...")

def get_directory_size(path):
    total_size = 0
    try:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                total_size += os.path.getsize(filepath)
    except OSError:
        pass
    return total_size / (1024 ** 2)  # 크기를 MB로 변환

def get_file_tree(path, indent="", output_file=None, max_depth=None, current_depth=0):
    try:
        entries = os.listdir(path)
    except OSError:
        entries = []

    for entry in entries:
        full_path = os.path.join(path, entry)

        if os.path.isdir(full_path):
            dir_size = get_directory_size(full_path)
            if dir_size > 0:
                output_file.write(f"{indent}- {entry} {dir_size:.3f}MB\n")
                if max_depth is None or current_depth < max_depth:
                    get_file_tree(full_path, indent + "|  ", output_file, max_depth, current_depth + 1)
        elif os.path.isfile(full_path):
            size = os.path.getsize(full_path) / (1024 ** 2)  # 크기를 MB로 변환
            output_file.write(f"{indent}- {entry} {size:.3f}MB\n")

def get_directory_tree(path, indent="", output_file=None, max_depth=None, current_depth=0):
    try:
        entries = os.listdir(path)
    except OSError:
        entries = []

    total_size = 0
    for entry in entries:
        full_path = os.path.join(path, entry)

        if os.path.isdir(full_path):
            dir_size = get_directory_size(full_path)
            if dir_size > 0:
                output_file.write(f"{indent}- {entry} {dir_size:.3f}MB\n")
                if max_depth is None or current_depth < max_depth:
                    total_size += dir_size
                    total_size += get_directory_tree(full_path, indent + "|  ", output_file, max_depth, current_depth + 1)

    return total_size

def main():
    print("Loading Done")
    print("On the Job...")
    start_total_time = time.time()

    parser = argparse.ArgumentParser(description='Generate a directory or file tree and export to a text file.')
    parser.add_argument('root_directory', type=str, help='Root directory path')
    parser.add_argument('-f', '--file_tree', action='store_true', help='Generate file tree')
    parser.add_argument('-d', '--directory_tree', action='store_true', help='Generate directory tree (default)')
    parser.add_argument('-o', '--output_file', type=str, help='Output file path (default is console)')
    parser.add_argument('-l', '--depth', type=int, help='Specify the depth of directory tree to display')
    args = parser.parse_args()

    root_directory = args.root_directory

    if args.output_file:
        with open(args.output_file, 'w') as output_file:
            start_dir_time = time.time()
            dir_size = get_directory_size(root_directory)
            if dir_size > 0:
                output_file.write(f"{root_directory} {dir_size:.3f}MB\n")
                if args.file_tree:
                    get_file_tree(root_directory, output_file=output_file, max_depth=args.depth)
                else:
                    total_size = get_directory_tree(root_directory, output_file=output_file, max_depth=args.depth)
                    print(f"Total size of {root_directory}: {total_size:.3f}MB")
            end_dir_time = time.time()
            elapsed_dir_time = end_dir_time - start_dir_time
            print(f"Directory tree generation time: {elapsed_dir_time:.4f} seconds")
    else:
        start_console_time = time.time()
        dir_size = get_directory_size(root_directory)
        if dir_size > 0:
            print(f"{root_directory} {dir_size:.3f}MB")
            if args.file_tree:
                get_file_tree(root_directory, max_depth=args.depth)
            else:
                total_size = get_directory_tree(root_directory, max_depth=args.depth)
                print(f"Total size of {root_directory}: {total_size:.3f}MB")
        end_console_time = time.time()
        elapsed_console_time = end_console_time - start_console_time
        print(f"Console output time: {elapsed_console_time:.4f} seconds")

    end_total_time = time.time()
    elapsed_total_time = end_total_time - start_total_time
    print(f"Total execution time: {elapsed_total_time:.4f} seconds")

if __name__ == "__main__":
    main()
    print("Job Done.")
    print("Thank you.")