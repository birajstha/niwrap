# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

GET_LABEL_THICKNESS_METADATA = Metadata(
    id="dee540c5d6addffa9eea35a7fd1572afd491a587.boutiques",
    name="get_label_thickness",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class GetLabelThicknessOutputs(typing.NamedTuple):
    """
    Output object returned when calling `get_label_thickness(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def get_label_thickness(
    infile: InputPathType,
    runner: Runner | None = None,
) -> GetLabelThicknessOutputs:
    """
    Tool to calculate label thickness.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        infile: Input file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GetLabelThicknessOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(GET_LABEL_THICKNESS_METADATA)
    cargs = []
    cargs.append("get_label_thickness")
    cargs.append(execution.input_file(infile))
    cargs.append("[OPTIONS]")
    ret = GetLabelThicknessOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "GET_LABEL_THICKNESS_METADATA",
    "GetLabelThicknessOutputs",
    "get_label_thickness",
]