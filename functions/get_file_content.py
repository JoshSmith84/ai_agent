import os
from config import *
from functions.validate_path import validate_path


def get_file_content(working_directory: str, file_path: str) -> str:
    """Read contents of a file truncated to MAX_CHARS config variable
    
    :param working_directory: Working Directory where the target file resides
    :param file_path: The filename to open (realtive path)
    :return: A string of file contents if readable
    """
        
    validated_path, fail_check = validate_path(working_directory, file_path)            

    if fail_check == 1:
        return f'Error: Cannot read "{file_path}" as it is ' \
                'outside the permitted working directory'     
    
    if os.path.isfile(validated_path) == False:
            return f'Error: File not found or is not a regular file: "{file_path}"'
    
    with open(validated_path, 'r') as file:
        contents = file.read(MAX_CHARS)

        if file.read(1):
            contents += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        
    return contents