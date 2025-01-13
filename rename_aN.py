import os


def rename_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        files.sort()  # To ensure consistent ordering

        for index, file in enumerate(files):
            file_path = os.path.join(folder_path, file)
            new_file_name = f"a{index + 1}{os.path.splitext(file)[1]}"
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(file_path, new_file_path)
            print(f"Renamed {file_path} to {new_file_path}")

        print("All files have been renamed successfully.")

    except Exception as e:
        print(f"Error renaming files: {e}")


folder_path = r'G:\facebook\videos'
rename_files_in_folder(folder_path)
