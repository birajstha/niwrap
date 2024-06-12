# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

ZEROPAD_METADATA = Metadata(
    id="1b8a4fe549da02c8b09a23d661165bcba26477eb",
    name="zeropad",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="local/zeropad:latest",
)


class ZeropadOutputs(typing.NamedTuple):
    """
    Output object returned when calling `zeropad(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def zeropad(
    input_number: str,
    output_length: float | int,
    runner: Runner = None,
) -> ZeropadOutputs:
    """
    zeropad.
    
    Add leading zeros to a number up to the specified length.
    
    Args:
        input_number: Input number to pad.
        output_length: Desired length of output with leading zeros.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ZeropadOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ZEROPAD_METADATA)
    cargs = []
    cargs.append("zeropad")
    cargs.append(input_number)
    cargs.append(str(output_length))
    ret = ZeropadOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ZEROPAD_METADATA",
    "ZeropadOutputs",
    "zeropad",
]
