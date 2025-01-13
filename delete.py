#merge same sized files


import os
from collections import defaultdict


def find_files_with_same_size(folder_path):
    size_dict = defaultdict(list)
    print(f"Walking through the directory: {folder_path}")

    try:
        for root, _, files in os.walk(folder_path):
            print(f"Currently in directory: {root}")
            for file in files:
                try:
                    file_path = os.path.join(root, file)
                    file_size = os.path.getsize(file_path)
                    size_dict[file_size].append(file_path)
                    print(f"Processed file: {file_path} with size: {file_size} bytes")
                except Exception as e:
                    print(f"Error processing file {file}: {e}")

        for size, paths in size_dict.items():
            if len(paths) > 1:
                print(f"Keeping {paths[0]} and deleting the rest...")
                for file_path in paths[1:]:
                    os.remove(file_path)
                    print(f"Deleted {file_path}")

        print("Operation completed.")

    except Exception as e:
        print(f"Error accessing folder {folder_path}: {e}")

# folder location here
folder_path = r'G:\facebook\videos'
find_files_with_same_size(folder_path)
