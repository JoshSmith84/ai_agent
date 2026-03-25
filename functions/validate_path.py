import os


def validate_path(working_directory: str, target_path: str) -> tuple:
    """Run checks on a target file/folder
    
    :param working_directory: parent folder to search
    :param target_path: The file/folder to validate
    :return: A tuple containing the target_path as absolute path 
    and a 0 or 1 based on whether or not it failed the commonpath check"""

    common_path = 0
    working_dir_abs = os.path.abspath(working_directory)
    abs_target_path = os.path.normpath(
        os.path.join(working_dir_abs, target_path)
        )
    
    if os.path.commonpath(
        [working_dir_abs, abs_target_path]
        ) != working_dir_abs:
        common_path = 1
    
    return abs_target_path, common_path