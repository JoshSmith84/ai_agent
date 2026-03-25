import os
from functions.validate_path import validate_path


def get_files_info(working_directory: str, directory=".") -> str:
    """Get info on all files in a directory
    
    :param working_directory: parent directory
    :param directory: Folder to search
    "return: String containing file/folder names, size, 
    and if it is a directory. Formatted neatly
    """


    validated_path, fail_check = validate_path(working_directory, directory)

    if fail_check == 1:
        return f'Error: Cannot list "{directory}" as it is ' \
                'outside the permitted working directory' 

    if os.path.isdir(validated_path) == False:
        return f'Error: "{validated_path}" is not a directory'
    
    content_string = ''
    for i in os.listdir(validated_path):
        abs_i = '/'.join([validated_path, i])
        try:
            current_i_size = os.path.getsize(abs_i)
        except:
            OSError(f"Error: {i} does not exist or is inaccessible.")
        
        try:
            current_i_isdir = os.path.isdir(abs_i)
        except:
            Exception(f"Error: {i} does not exist or is inaccessible.")

        content_string += f"- {i}: " \
        f"file_size={current_i_size} bytes, " \
        f"is_dir={current_i_isdir}\n"

    return content_string