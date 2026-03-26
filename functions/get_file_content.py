import os
from google import genai
from google.genai import types
from config import *
from functions.validate_path import validate_path


schema_get_file_content= types.FunctionDeclaration(
    name="get_file_content",
    description="Open and read contents of a file in the working directory, returning the output as a string",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Filename of contents to read.",
            ),
        },
    ),
)


def get_file_content(working_directory: str, file_path: str) -> str:
    """Read contents of a file truncated to MAX_CHARS config variable
    
    :param working_directory: Working Directory where the target file resides
    :param file_path: The filename to open (realtive path)
    :return: A string of file contents if readable
    """
        
    validated_path, workdir_abs, fail_check = validate_path(
         working_directory, file_path
           )            

    if fail_check == 1:
        return f'Error: Cannot read "{file_path}" as it is ' \
                'outside the permitted working directory'     
    
    if os.path.isfile(validated_path) == False:
            return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(validated_path, 'r') as file:
            contents = file.read(MAX_CHARS)

        if file.read(1):
            contents += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    except Exception as e:
         return f"Error: {e}" 
    
    return contents