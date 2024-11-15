import os

def change_extension(directory, old_ext, new_ext):
    """
    Change file extensions in the specified directory from old_ext to new_ext.
    
    Parameters:
    directory (str): The path to the directory containing the files.
    old_ext (str): The current file extension (e.g., '.txt').
    new_ext (str): The new file extension (e.g., '.md').
    """
    
    # Iterate over files in the directory
    for filename in os.listdir(directory):
        # Check if the file has the old extension
        if filename.endswith(old_ext):
            # Construct the new filename
            new_filename = filename[:-len(old_ext)] + new_ext
            # Rename the file
            os.rename(
                os.path.join(directory, filename),
                os.path.join(directory, new_filename)
            )
            print(f'Renamed: {filename} -> {new_filename}')

ex_to_ch = input("Enter Extention to Change: ")
ex_to = input("Enter Extention to Change to: ")
dir = input("Enter the dir: ")
change_extension(dir, ex_to_ch, ex_to)
# Example usage:
# change_extension('/path/to/your/directory', '.txt', '.md')
