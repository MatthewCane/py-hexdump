from pathlib import Path
from subprocess import CalledProcessError, run

import pytest

from py_hexdump import hexdump


def gnu_hexdump(file: str) -> str:
    """
    Run gnu hexdump and return the results.
    """
    try:
        return run(
            f"hexdump -C {file}",
            shell=True,  # Use the default system shell (bash, zsh, e.t.c)
            capture_output=True,  # Capture stdout and stderr
            text=True,  # Decode output bytes into strings
            check=True,  # Raises an error on non-zero return code
        ).stdout.strip()

    except CalledProcessError as e:
        error_message = f"Command failed with exit code {e.returncode}\n"
        error_message += f"stdout: {e.stdout}\n"
        error_message += f"stderr: {e.stderr}"
        raise RuntimeError(error_message) from e


# Collect all test files in the tests/test_files directory
test_files = Path("tests/test_files").glob("*")


@pytest.mark.parametrize("path", test_files, ids=lambda x: x.name)
def test_string(path: str):
    """Test hexdump output against GNU hexdump for various files.

    The ids parameter is used to give each test a meaningful name
    based on the file name. This needs to be a callable (lambda function
    in this case)
    """
    p = Path(path).absolute()

    with p.open("rb") as f:
        pyhd = hexdump(f.read(), output=None)

    assert pyhd == gnu_hexdump(str(p))
