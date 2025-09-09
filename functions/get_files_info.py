import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    working_real = os.path.realpath(working_directory)
    target_real = os.path.realpath(os.path.join(working_directory, directory))
    if not (target_real == working_real or target_real.startswith(working_real + os.sep)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif not os.path.isdir(target_real):
        return f'Error: "{directory}" is not a directory'
    try:
        entries = os.listdir(target_real)
        lines = []
        for name in entries:
            full = os.path.join(target_real, name)
            is_dir = os.path.isdir(full)
            size = os.path.getsize(full)
            lines.append(f'- {name}: file_size={size} bytes, is_dir={is_dir}')
        return '\n'.join(lines)
    except Exception as e:
        return f'Error: {e}'

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)