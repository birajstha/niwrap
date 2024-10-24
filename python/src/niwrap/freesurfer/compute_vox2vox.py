# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

COMPUTE_VOX2VOX_METADATA = Metadata(
    id="cac931a71ca00f1e6fd4a05be9aebaf5ca0482ec.boutiques",
    name="compute_vox2vox",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class ComputeVox2voxOutputs(typing.NamedTuple):
    """
    Output object returned when calling `compute_vox2vox(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """The resulting transformed voxel-to-voxel 4dfp output file."""


def compute_vox2vox(
    source: InputPathType,
    t4file: InputPathType,
    target: InputPathType,
    runner: Runner | None = None,
) -> ComputeVox2voxOutputs:
    """
    Tool for computing voxel-to-voxel transformations.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        source: Input 4dfp source file.
        t4file: T4 transformation matrix file.
        target: Input 4dfp target file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ComputeVox2voxOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(COMPUTE_VOX2VOX_METADATA)
    cargs = []
    cargs.append("compute_vox2vox")
    cargs.append(execution.input_file(source))
    cargs.append(execution.input_file(t4file))
    cargs.append(execution.input_file(target))
    ret = ComputeVox2voxOutputs(
        root=execution.output_file("."),
        output=execution.output_file("<replace_with_output_path_pattern>"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "COMPUTE_VOX2VOX_METADATA",
    "ComputeVox2voxOutputs",
    "compute_vox2vox",
]
