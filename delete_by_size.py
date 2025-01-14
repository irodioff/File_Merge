import os
import stat

# Set the top-level folder path
top_folder_path = r'E:\unz tkout\Google Photos'

# Walk through all directories and subdirectories
for root, dirs, files in os.walk(top_folder_path):
    for filename in files:
        file_path = os.path.join(root, filename)
        try:
            # Check if the file exists
            if os.path.exists(file_path):
                file_size = os.path.getsize(file_path)
                if file_size < 1200:
                    # Remove read-only attribute and change file permissions
                    os.chmod(file_path, stat.S_IWRITE)
                    os.remove(file_path)
                    print(f'Deleted: {file_path}')
                else:
                    print(f'Skipped (File too large): {file_path} (Size: {file_size} bytes)')
            else:
                print(f'Skipped (File does not exist): {file_path}')
        except PermissionError:
            print(f'Skipped (Permission Denied): {file_path}')
        except Exception as e:
            print(f'Skipped ({e}): {file_path}')

print('Attempted to delete all files less than 1200 bytes.')
