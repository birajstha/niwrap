# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

MCCUTUP_METADATA = Metadata(
    id="c81cbc917b8577f52dfd5b7d82a0002855a8041c",
    name="mccutup",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="fsl_image",
)


class MccutupOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mccutup(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType | None
    """Output file"""


def mccutup(
    input_: InputPathType,
    output_file: str | None = None,
    param1: str | None = None,
    param2: str | None = None,
    runner: Runner = None,
) -> MccutupOutputs:
    """
    mccutup by FSL.
    
    FSL mccutup tool.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/
    
    Args:
        input_: Input file
        output_file: Specify output file name
        param1: Parameter 1 description
        param2: Parameter 2 description
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `MccutupOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MCCUTUP_METADATA)
    cargs = []
    cargs.append("/usr/local/fsl/bin/mccutup")
    cargs.append("[OPTIONS]")
    cargs.append(execution.input_file(input_))
    ret = MccutupOutputs(
        root=execution.output_file("."),
        output=execution.output_file(f"{output_file}", optional=True) if output_file is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MCCUTUP_METADATA",
    "MccutupOutputs",
    "mccutup",
]
