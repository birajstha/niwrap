# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MAKE_EXVIVO_FILLED_METADATA = Metadata(
    id="ea9e6e6bb03c9eb7e7861ad8386b4df6348f9898.boutiques",
    name="make_exvivo_filled",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MakeExvivoFilledOutputs(typing.NamedTuple):
    """
    Output object returned when calling `make_exvivo_filled(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def make_exvivo_filled(
    subject_name: str,
    input_samseg: InputPathType,
    input_intensity_vol: InputPathType,
    hemi_both: str,
    runner: Runner | None = None,
) -> MakeExvivoFilledOutputs:
    """
    A command-line tool for generating filled ex vivo brain images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_name: Name of the subject.
        input_samseg: Input SAMSEG (Segmentation Analysis of MRI brain images).
        input_intensity_vol: Input intensity volume.
        hemi_both: Specify hemisphere or both.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MakeExvivoFilledOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MAKE_EXVIVO_FILLED_METADATA)
    cargs = []
    cargs.append("make_exvivo_filled")
    cargs.append(subject_name)
    cargs.append(execution.input_file(input_samseg))
    cargs.append(execution.input_file(input_intensity_vol))
    cargs.append(hemi_both)
    ret = MakeExvivoFilledOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MAKE_EXVIVO_FILLED_METADATA",
    "MakeExvivoFilledOutputs",
    "make_exvivo_filled",
]