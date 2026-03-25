import os


def get_files_info(working_directory, directory="."):

    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(
        os.path.join(working_dir_abs, directory)
        )
    
    if os.path.commonpath(
        [working_dir_abs, target_dir]
        ) != working_dir_abs:
        return f'Error: Cannot list "{directory}" as it is ' \
                'outside the permitted working directory'
            
    if os.path.isdir(target_dir) == False:
        return f'Error: "{target_dir}" is not a directory'
    
    print(target_dir)
    content_string = ''
    for i in os.listdir(target_dir):
        abs_i = '/'.join([target_dir, i])
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