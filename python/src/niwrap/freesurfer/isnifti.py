# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ISNIFTI_METADATA = Metadata(
    id="0ec07279947545d1155748f4d9a448ee304204a0.boutiques",
    name="isnifti",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class IsniftiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `isnifti(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def isnifti(
    infile: InputPathType,
    runner: Runner | None = None,
) -> IsniftiOutputs:
    """
    A simple tool to check if a file is a NIfTI image.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        infile: Input file to be checked if it is a NIfTI image.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `IsniftiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ISNIFTI_METADATA)
    cargs = []
    cargs.append("isnifti")
    cargs.append(execution.input_file(infile))
    ret = IsniftiOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ISNIFTI_METADATA",
    "IsniftiOutputs",
    "isnifti",
]
