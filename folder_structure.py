import os

def print_directory_tree(startpath, indent_level=0, include_first_level=None, exclude_folders=None):
    if include_first_level is None:
        include_first_level = {'app', 'test'}  # Include only these in the first iteration
    
    if exclude_folders is None:
        exclude_folders = {'.git', '__pycache__', 'image'}  # Exclude these folders in all iterations
    
    indent = ' ' * (4 * indent_level)  # Indentation for nested folders
    print(indent + os.path.basename(startpath) + '/')
    
    with os.scandir(startpath) as entries:
        for entry in entries:
            # First iteration: only include `path_a` and `path_b`
            if indent_level == 0 and entry.name not in include_first_level:
                continue
            
            # Skip excluded folders
            if entry.is_dir(follow_symlinks=False) and entry.name not in exclude_folders:
                print_directory_tree(entry.path, indent_level + 1, include_first_level, exclude_folders)
            elif entry.is_file(follow_symlinks=False):
                print(indent + ' ' * 4 + entry.name)

# Set the path to your project folder
project_path = os.path.abspath('.')

# Call the function to print the directory structure, including only `path_a` and `path_b` in the first iteration
print_directory_tree(project_path)
