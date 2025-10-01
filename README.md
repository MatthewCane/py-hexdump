# py-hexdump

A Python implementation of the `hexdump` command line utility with `-C` option.

This is purely an academic exercise to learn more about binary file handling in Python and should not be used for practical purposes.

```text
$ uv run src/py_hexdump .gitignore
00000000  23 20 50 79 74 68 6f 6e  2d 67 65 6e 65 72 61 74  |# Python-generat|
00000010  65 64 20 66 69 6c 65 73  0a 5f 5f 70 79 63 61 63  |ed files.__pycac|
00000020  68 65 5f 5f 2f 0a 2a 2e  70 79 5b 6f 63 5d 0a 62  |he__/.*.py[oc].b|
00000030  75 69 6c 64 2f 0a 64 69  73 74 2f 0a 77 68 65 65  |uild/.dist/.whee|
00000040  6c 73 2f 0a 2a 2e 65 67  67 2d 69 6e 66 6f 0a 0a  |ls/.*.egg-info..|
00000050  23 20 56 69 72 74 75 61  6c 20 65 6e 76 69 72 6f  |# Virtual enviro|
00000060  6e 6d 65 6e 74 73 0a 2e  76 65 6e 76 0a 0a 23 20  |nments..venv..# |
00000070  43 61 63 68 65 0a 2e 70  79 74 65 73 74 5f 63 61  |Cache..pytest_ca|
00000080  63 68 65 2f 0a 2e 72 75  66 66 5f 63 61 63 68 65  |che/..ruff_cache|
00000090  2f                                                |/|
00000091
```

## Usage

This can be used as a command line utility or as a Python module. It will attempt to mimic the output of `hexdump -C` as closely as possible.

### Command Line

```bash
uv run src/hexdump <file>
```

It accepts the following:

- **--width**: Number of groups of 8 bytes to display per row (default: 2)
- **--encoding**: Encoding to use for the ASCII representation (default: system default)

### Python Module

```python
from hexdump import hexdump

with open("file", "rb") as f:
    print(hexdump(f))
```

## Testing

Tests are provided to compare the output of this implementation against `hexdump -C` for various files in the `tests/test_files` directory.
