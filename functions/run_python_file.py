import os
import subprocess

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