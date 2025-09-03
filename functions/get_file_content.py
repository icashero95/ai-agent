import os
import config

def get_file_content(working_directory, file_path):
    working_real = os.path.realpath(working_directory)
    target_real = os.path.realpath(os.path.join(working_directory, file_path))
    if not (target_real == working_real or target_real.startswith(working_real + os.sep)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    elif not os.path.isfile(target_real):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(target_real, "r") as f:
            file_content_string = f.read()
            if len(file_content_string) > config.MAX_CHARS:
                truncated_file_content_string = file_content_string[:config.MAX_CHARS]
                truncated_file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
                return truncated_file_content_string
            return file_content_string
    except Exception as e:
        return f'Error: {e}'
    