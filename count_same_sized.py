import os
from collections import defaultdict


def find_files_with_same_size(folder_path):
    size_dict = defaultdict(list)

    try:
        for root, _, files in os.walk(folder_path):
            for file in files:
                try:
                    file_path = os.path.join(root, file)
                    file_size = os.path.getsize(file_path)
                    size_dict[file_size].append(file_path)
                except Exception as e:
                    print(f"Error processing file {file}: {e}")

        same_size_files = {size: len(paths) for size, paths in size_dict.items() if len(paths) > 1}

        if not same_size_files:
            print("No files with the same size found.")
        else:
            for size, count in same_size_files.items():
                print(f"There are {count} files with size {size} bytes")

    except Exception as e:
        print(f"Error accessing folder {folder_path}: {e}")


folder_path = r'G:\facebook\videos'
find_files_with_same_size(folder_path)
