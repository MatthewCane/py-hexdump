# py-hexdump

A Python implementation of the `hexdump` command line utility with `-C` option.

This is purely an academic exercise to learn more about binary file handling in Python and should not be used for practical purposes.

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
