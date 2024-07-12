# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

IMCP_METADATA = Metadata(
    id="b466c0d803c6e1b2b3b58f1ff6ec00b6ffb02ea0",
    name="imcp",
)


class ImcpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `imcp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfiles: OutputPathType
    """Output file or directory"""


def imcp(
    infiles: list[InputPathType],
    output_location: str,
    runner: Runner | None = None,
) -> ImcpOutputs:
    """
    imcp by Unknown.
    
    Copy images from one location to another.
    
    Args:
        infiles: Input image files (e.g. img1.nii.gz, img2.nii.gz).
        output_location: Output file or directory.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ImcpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IMCP_METADATA)
    cargs = []
    cargs.append("imcp")
    cargs.extend([execution.input_file(f) for f in infiles])
    cargs.append(output_location)
    ret = ImcpOutputs(
        root=execution.output_file("."),
        outfiles=execution.output_file(f"{output_location}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "IMCP_METADATA",
    "ImcpOutputs",
    "imcp",
]
