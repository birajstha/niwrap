# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TALAIRACH2_METADATA = Metadata(
    id="200a3bdd395b88d5b03ecdc9cf8d79338e29d2f2.boutiques",
    name="talairach2",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class Talairach2Outputs(typing.NamedTuple):
    """
    Output object returned when calling `talairach2(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def talairach2(
    subject_id: str,
    mgz_flag: str | None = None,
    runner: Runner | None = None,
) -> Talairach2Outputs:
    """
    Tool for processing and converting talairach transformation files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_id: Subject identifier for the talairach transformation.
        mgz_flag: Flag to indicate whether mgz format is used.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Talairach2Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TALAIRACH2_METADATA)
    cargs = []
    cargs.append("talairach2")
    cargs.append(subject_id)
    if mgz_flag is not None:
        cargs.append(mgz_flag)
    ret = Talairach2Outputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TALAIRACH2_METADATA",
    "Talairach2Outputs",
    "talairach2",
]