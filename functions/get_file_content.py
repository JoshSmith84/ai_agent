import os
from config import *


def get_file_content(working_directory, file_path):
        
    working_dir_abs = os.path.abspath(working_directory)    
    full_file_path = '/'.join([working_dir_abs, file_path])    

    if os.path.commonpath([working_dir_abs, 
                            full_file_path,
                            ]) != working_dir_abs:
        return f'Error: Cannot read "{file_path}" as it is ' \
                'outside the permitted working directory'
    
    if os.path.isfile(full_file_path) == False:
            return f'Error: File not found or is not a regular file: "{file_path}"'
    
    with open(full_file_path, 'r') as file:
        contents = file.read(MAX_CHARS)

        if file.read(1):
            contents += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        
    return contents