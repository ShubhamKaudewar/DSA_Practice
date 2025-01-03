import os

# Specify the folder path
folder_path = r"D:\Files\Coding\DSA_Practice\Leetcode"

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a Python file and contains space in its name
    if filename.endswith(".py") and " " in filename:
        # Create the new filename with spaces replaced by underscores
        new_filename = filename.replace(" ", "_")

        # Get the full paths for rename operation
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_filename)

        # Rename the file
        os.rename(old_file, new_file)
        print(f'Renamed: "{filename}" to "{new_filename}"')

print("All applicable files have been renamed.")