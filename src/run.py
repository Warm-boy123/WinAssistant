import subprocess


def run_cmd(string):
    command = string.split()
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
    if result.stderr:
        raise Exception(result.stderr)
    return result.stdout

# print(run_cmd("taskmgr"))
