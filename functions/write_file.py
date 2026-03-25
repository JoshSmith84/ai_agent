import os
from functions.validate_path import validate_path


def write_file(working_directory: str, file_path: str, content: str) -> str:
    """Function to (over)-write contents to file
    
    :param working_directory: Directory where target file/path resides
    :param file_path: The realtive path of the target
    :return: Completion status as a string"""
    
    validated_path, working_dir_abs, fail_check = validate_path(
        working_directory, file_path
        )

    if fail_check == 1:
        return f'Error: Cannot write to "{file_path}" '  \
                'as it is outside the permitted working directory'
 
    if os.path.isdir(validated_path):
        return f'Error: Cannot write to "{file_path}" ' \
                'as it is a directory'
    
    os.makedirs(working_dir_abs, exist_ok=True)

    try:
        with open(validated_path, 'w') as file:
            file.write(content)
    except Exception as e:
        return f"Error: {e}"
        
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'