# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_TOPOLOGYCORRECTION_METADATA = Metadata(
    id="fb398c893ff0a9507f05f5c97dc95a403a3121a3.boutiques",
    name="mri_topologycorrection",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriTopologycorrectionOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_topologycorrection(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_folder: OutputPathType
    """Directory where output files will be stored."""


def mri_topologycorrection(
    input_orig_file: InputPathType,
    input_segmented_file: InputPathType,
    runner: Runner | None = None,
) -> MriTopologycorrectionOutputs:
    """
    Corrects the topology of segmented MRI images.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_orig_file: Path to the original image file.
        input_segmented_file: Path to the segmented image file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriTopologycorrectionOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_TOPOLOGYCORRECTION_METADATA)
    cargs = []
    cargs.append("mri_topologycorrection")
    cargs.append(execution.input_file(input_orig_file))
    cargs.append(execution.input_file(input_segmented_file))
    ret = MriTopologycorrectionOutputs(
        root=execution.output_file("."),
        output_folder=execution.output_file("[OUTPUT_FOLDER]"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_TOPOLOGYCORRECTION_METADATA",
    "MriTopologycorrectionOutputs",
    "mri_topologycorrection",
]
