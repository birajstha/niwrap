# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_VESSEL_SEGMENT_METADATA = Metadata(
    id="6f3e4e326255b57c2dfda638c29cce61255996ef.boutiques",
    name="mri_vessel_segment",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriVesselSegmentOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_vessel_segment(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    segmented_output: OutputPathType
    """Segmented vessel output file"""


def mri_vessel_segment(
    t1_image: InputPathType,
    t2_image: InputPathType,
    aseg_file: InputPathType,
    output_file: str,
    shape_flag: bool = False,
    runner: Runner | None = None,
) -> MriVesselSegmentOutputs:
    """
    MRI vessel segmentation tool.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        t1_image: T1-weighted input image.
        t2_image: T2-weighted input image.
        aseg_file: Anatomical segmentation file.
        output_file: Output file.
        shape_flag: Use shape constraints during segmentation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriVesselSegmentOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_VESSEL_SEGMENT_METADATA)
    cargs = []
    cargs.append("mri_vessel_segment")
    cargs.extend([
        "-t1",
        execution.input_file(t1_image)
    ])
    cargs.extend([
        "-t2",
        execution.input_file(t2_image)
    ])
    cargs.extend([
        "-aseg",
        execution.input_file(aseg_file)
    ])
    cargs.extend([
        "-o",
        output_file
    ])
    if shape_flag:
        cargs.append("--shape")
    ret = MriVesselSegmentOutputs(
        root=execution.output_file("."),
        segmented_output=execution.output_file(output_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_VESSEL_SEGMENT_METADATA",
    "MriVesselSegmentOutputs",
    "mri_vessel_segment",
]
