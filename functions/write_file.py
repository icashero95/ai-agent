import os
from google.genai import types

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
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes, or overwrites, the content supplied to the funtion onto a file that is specified, which the function creates if it does not exist, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path to the file that needs to be written or overwritten.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content that must be written or overwritten to the file."
            ),
        },
        required=["file_path", "content"],
    ),
)