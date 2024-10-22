# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_AND_METADATA = Metadata(
    id="d8999cb2469425ecddc28cae1670605c1b9b54e1.boutiques",
    name="mri_and",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriAndOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_and(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_and(
    input_files: list[InputPathType],
    runner: Runner | None = None,
) -> MriAndOutputs:
    """
    Performs a logical voxel-wise AND on a series of volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_files: Input volume files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriAndOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_AND_METADATA)
    cargs = []
    cargs.append("/usr/local/freesurfer/bin/mri_and")
    cargs.extend([execution.input_file(f) for f in input_files])
    ret = MriAndOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_AND_METADATA",
    "MriAndOutputs",
    "mri_and",
]