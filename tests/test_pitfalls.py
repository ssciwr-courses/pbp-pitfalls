import pytest
import re
import subprocess
from pathlib import Path


def test_import():
    # Get the repository directory
    current_dir = Path(__file__).resolve().parents[1]
    input_file_path = current_dir / "chapter4"
    # get the python files
    python_modules = list(input_file_path.glob('*.py'))
    # try to run the math module:
    # find the item in the list that has the math module
    matches = [i for i, item in enumerate(python_modules) if re.findall("math", item.name) != []]
    # list should have exactly one item, but if not, we will take the first one
    # if it is empty, raise error
    assert len(matches) >= 1
    # now try to run python on the first match
    command = "python {}".format(python_modules[matches[0]])
    failure = 0 
    try:
        subprocess.check_output(command, shell=True)
    except subprocess.CalledProcessError as e:
        failure = e.returncode
    if failure != 0:
        print("Error: Could not run Python on {}".format(python_modules[matches[0]]))
    assert failure == 0
