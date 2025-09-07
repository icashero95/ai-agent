import os

def write_file(working_directory, file_path, content):
    working_real = os.path.realpath(working_directory)
    target_real = os.path.realpath(os.path.join(working_directory, file_path))
    if not (target_real == working_real or target_real.startswith(working_real + os.sep)):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        os.makedirs(os.path.dirname(target_real), exist_ok=True)
        with open(target_real, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e}'