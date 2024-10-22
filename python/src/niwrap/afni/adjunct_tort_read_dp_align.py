# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ADJUNCT_TORT_READ_DP_ALIGN_METADATA = Metadata(
    id="336b17b39a158c5e3a7cfad25b946bfcc915ab71.boutiques",
    name="adjunct_tort_read_dp_align",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class AdjunctTortReadDpAlignOutputs(typing.NamedTuple):
    """
    Output object returned when calling `adjunct_tort_read_dp_align(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Output '1D' file in AFNI format with translation and rotation
    parameters."""


def adjunct_tort_read_dp_align(
    input_file: InputPathType,
    output_file: InputPathType,
    runner: Runner | None = None,
) -> AdjunctTortReadDpAlignOutputs:
    """
    Extract the 3 translation (in mm) and 3 rotation (in deg) parameters estimated
    by TORTOISE's DIFF_PREP tool during DWI processing.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/adjunct_tort_read_dp_align.py.html
    
    Args:
        input_file: Input *_transformations.txt file output by TORTOISE's\
            DIFF_PREP.
        output_file: Output '1D' file in AFNI format. A text file with 6\
            columns representing translation and rotation parameters.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AdjunctTortReadDpAlignOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ADJUNCT_TORT_READ_DP_ALIGN_METADATA)
    cargs = []
    cargs.append("adjunct_tort_read_mot_transforms.py")
    cargs.append(execution.input_file(input_file))
    cargs.append(execution.input_file(output_file))
    ret = AdjunctTortReadDpAlignOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(pathlib.Path(output_file).name),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ADJUNCT_TORT_READ_DP_ALIGN_METADATA",
    "AdjunctTortReadDpAlignOutputs",
    "adjunct_tort_read_dp_align",
]