from itertools import batched
from locale import getpreferredencoding
from sys import stdout
from typing import TYPE_CHECKING, Optional

from bitarray import bitarray
from bitarray.util import ba2hex
from tabulate import tabulate

if TYPE_CHECKING:
    from _typeshed import SupportsWrite


def hexdump(
    data: str | bytes | bytearray | memoryview,
    width: int = 2,
    encoding: str | None = None,
    output: Optional["SupportsWrite"] = stdout,
) -> str:
    COLS = width
    CHUNK_WIDTH = 8 * COLS
    DEFAULT_CHAR = "."

    encoding = encoding or getpreferredencoding()

    if isinstance(data, str):
        bits = bitarray(data.encode(encoding=encoding))
    elif isinstance(data, bytes | bytearray):
        bits = bitarray(data)
    elif isinstance(data, memoryview):
        bits = bitarray(bytearray(data))
    else:
        raise TypeError(
            "Argument data must be of type string, bytes, bytearray or memoryview"
        )

    def calculate_offset(chunk_number, offset=0) -> str:
        return str(hex((chunk_number * CHUNK_WIDTH) + offset))[2:].zfill(8)

    details = []

    for chunk_number, chunk_bits in enumerate(batched(bits, 8 * CHUNK_WIDTH)):
        # Convert the chunk of bits to a bitarray
        chunk_bits = bitarray(chunk_bits)
        # Calculate the offset, convert to hex and fill in the empty space
        offset = calculate_offset(chunk_number)

        # Split the bits into bytes seperated by a space
        hexed_chunk = " ".join(
            ["".join(str(ba2hex(bitarray(b)))) for b in batched(chunk_bits, 8)]
        )
        # Split the hex bytes into columns of 8 bytes
        hexed_chunks = ["".join(c) for c in batched(hexed_chunk, 24)]
        while len(hexed_chunks) < COLS:
            hexed_chunks.append("")

        # Decode the chunk byte by byte and replace non-printable characters
        decoded_chunk = ""
        for byte in batched(chunk_bits, 8):
            byte = bitarray(byte)
            try:
                decoded_chunk = decoded_chunk + byte.tobytes().decode(encoding)
            except UnicodeDecodeError:
                decoded_chunk = decoded_chunk + DEFAULT_CHAR

        # Replace all unprintable ascii chars with � char
        unprintable = [chr(i) for i in range(0, 32)]
        unprintable.append(chr(127))
        for c in unprintable:
            decoded_chunk = decoded_chunk.replace(c, DEFAULT_CHAR)

        # Add the row to the details array, unpacking the list of chunked hex values
        details.append((offset, *hexed_chunks, f"|{decoded_chunk}|"))

    # Add final offset row to output
    details.append(
        (
            calculate_offset(
                chunk_number,
                offset=len(decoded_chunk),
            ),
        )
    )

    table = tabulate(tabular_data=details, tablefmt="plain")

    if output:
        print(table, end=None, file=output)

    return table
