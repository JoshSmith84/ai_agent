import os
import subprocess
from google import genai
from google.genai import types
from functions.validate_path import validate_path


schema_run_python_file= types.FunctionDeclaration(
    name="run_python_file",
    description="Execute a python file in the working directory, returning the exit code and any standard/error output as a string",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Python filename to to run.",
            ),
        },
    ),
)


def run_python_file(working_directory: str, file_path: str, args=None) -> str:
    """Function to run a Py file
    
    :param working_directory: Working directory of target script
    :param file_path: target script
    :param args: potentially list of arguments to pass to script.
    """

    validated_path, workdir_abs, fail_check = validate_path(
        working_directory, file_path
        )

    if fail_check == 1:
        return f'Error: Cannot execute "{file_path}" ' \
                'as it is outside the permitted working directory'
    
    if os.path.isfile(validated_path) == False:
        return f'Error: "{file_path}" does not exist ' \
                'or is not a regular file'
    
    if validated_path.endswith('.py') == False:
        return f'Error: "{file_path}" is not a Python file'
    
    command = ["python", validated_path]

    if args:
        command.extend(args)

    try:
        completed_proc = subprocess.run(command, 
                                    cwd=workdir_abs, 
                                    text=True,
                                    timeout=30,
                                    capture_output=True
                                    )
    except Exception as e:
        return f"Error: executing Python file: {e}"

    proc_stdout = completed_proc.stdout
    proc_stderr = completed_proc.stderr
    proc_excode = completed_proc.returncode

    output = ''
    if proc_excode != 0:
        output += f"Process exited with code {proc_excode}\n"

    if proc_stdout == None and proc_stderr == None:
        output += "No output produced\n"
    else:
        output += f"STDOUT: {proc_stdout}\nSTDERR: {proc_stderr}\n"

    return output