# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

REG_AVERAGE_METADATA = Metadata(
    id="61e1f607541cf2b120dd32fdab5918c08f2dda1a.boutiques",
    name="reg_average",
    package="niftyreg",
    container_image_tag="vnmd/niftyreg_1.4.0:20220819",
)


class RegAverageOutputs(typing.NamedTuple):
    """
    Output object returned when calling `reg_average(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file_location: OutputPathType
    """The averaged output file (image or affine transformation)"""


def reg_average(
    output_file: str,
    input_files: list[InputPathType],
    runner: Runner | None = None,
) -> RegAverageOutputs:
    """
    Command line program to average either images or affine transformations.
    
    Author: NiftyReg Developers
    
    URL: http://cmictig.cs.ucl.ac.uk/wiki/index.php/NiftyReg
    
    Args:
        output_file: Filename of the output image or affine transformation.
        input_files: Input file names (images or affine matrices) to be\
            averaged.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RegAverageOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(REG_AVERAGE_METADATA)
    cargs = []
    cargs.append("reg_average")
    cargs.append(output_file)
    cargs.extend([execution.input_file(f) for f in input_files])
    ret = RegAverageOutputs(
        root=execution.output_file("."),
        output_file_location=execution.output_file(output_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "REG_AVERAGE_METADATA",
    "RegAverageOutputs",
    "reg_average",
]
