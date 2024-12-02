# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_FUSE_INTENSITY_IMAGES_METADATA = Metadata(
    id="b44314c2289888a92cbc6fcb500d2dc0bdb27bc9.boutiques",
    name="mri_fuse_intensity_images",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriFuseIntensityImagesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_fuse_intensity_images(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    fused_intensity_image: OutputPathType
    """The resulting fused intensity image"""


def mri_fuse_intensity_images(
    longitudinal_time_point_file: InputPathType,
    input_volume: InputPathType,
    transform_file: InputPathType,
    output_volume: InputPathType,
    runner: Runner | None = None,
) -> MriFuseIntensityImagesOutputs:
    """
    Fuses intensity images based on given transforms.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        longitudinal_time_point_file: File containing the longitudinal time\
            points.
        input_volume: Input volume to be fused.
        transform_file: File containing the transforms.
        output_volume: Output fused volume.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriFuseIntensityImagesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_FUSE_INTENSITY_IMAGES_METADATA)
    cargs = []
    cargs.append("mri_fuse_intensity_images")
    cargs.append(execution.input_file(longitudinal_time_point_file))
    cargs.append(execution.input_file(input_volume))
    cargs.append(execution.input_file(transform_file))
    cargs.append(execution.input_file(output_volume))
    ret = MriFuseIntensityImagesOutputs(
        root=execution.output_file("."),
        fused_intensity_image=execution.output_file(pathlib.Path(output_volume).name),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_FUSE_INTENSITY_IMAGES_METADATA",
    "MriFuseIntensityImagesOutputs",
    "mri_fuse_intensity_images",
]
