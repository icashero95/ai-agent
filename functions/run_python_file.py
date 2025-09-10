import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    working_real = os.path.realpath(working_directory)
    target_real = os.path.realpath(os.path.join(working_directory, file_path))
    if not target_real.startswith(working_real + os.sep):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    elif os.path.exists(target_real) == False:
        return f'Error: File "{file_path}" not found.'
    elif file_path.endswith(".py") == False:
        return f'Error: "{file_path}" is not a Python file.'
    cmd = ["python", target_real] + list(args)
    try:
        completed_process = subprocess.run(
            cmd,
            cwd=working_directory,
            capture_output=True,
            text=True,
            timeout=30
        )
        if (len(completed_process.stdout)) < 1 and (len(completed_process.stderr) < 1):
            return "No output produced."
        elif completed_process.returncode != 0:
            return f"STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}\nProcess exited with code {completed_process.returncode}"
        else:
            return f"STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}"
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Checks if the supplied file is an executable python file, then runs the code while constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative file path of where the executable pythin file is, relative to the working directory.",
            ),
        },
        required=["file_path"]
    ),
)