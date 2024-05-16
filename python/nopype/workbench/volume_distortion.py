# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:58:55.879025

import typing

from ..styxdefs import *


VOLUME_DISTORTION_METADATA = Metadata(
    id="4fb51858c63698643ab136ca3658a1de49d09c21",
    name="volume-distortion",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class VolumeDistortionOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_distortion(...)`.
    """
    volume_out: OutputPathType
    """the output distortion measures"""


def volume_distortion(
    runner: Runner,
    warpfield: str,
    volume_out: InputPathType,
    opt_fnirt_source_volume: str | None = None,
    opt_circular: bool = False,
    opt_log2: bool = False,
) -> VolumeDistortionOutputs:
    """
    CALCULATE VOLUME WARPFIELD DISTORTION.
    
    Calculates isotropic and anisotropic distortions in the volume warpfield. At
    each voxel, the gradient of the absolute warpfield is computed to obtain the
    local affine transforms for each voxel (jacobian matrices), and strain
    tensors are derived from them. The isotropic component (volumetric expansion
    ratio) is the product of the three principal strains. The default measure
    ('elongation') for the anisotropic component is the largest principal strain
    divided by the smallest.
    
    The -circular option instead calculates the anisotropic component by
    transforming the principal strains into log space, considering them as
    x-values of points on a circle 120 degrees apart, finds the circle's
    diameter, and transforms that back to a ratio.
    
    Args:
        runner: Command runner
        warpfield: the warpfield to compute the distortion of
        volume_out: the output distortion measures
        opt_fnirt_source_volume: MUST be used if using a fnirt warpfield: the
            source volume used when generating the warpfield
        opt_circular: use the circle-based formula for the anisotropic measure
        opt_log2: apply base-2 log transform
    Returns:
        NamedTuple of outputs (described in `VolumeDistortionOutputs`).
    """
    execution = runner.start_execution(VOLUME_DISTORTION_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-distortion")
    cargs.append(warpfield)
    cargs.append(execution.input_file(volume_out))
    if opt_fnirt_source_volume is not None:
        cargs.extend(["-fnirt", opt_fnirt_source_volume])
    if opt_circular:
        cargs.append("-circular")
    if opt_log2:
        cargs.append("-log2")
    ret = VolumeDistortionOutputs(
        volume_out=execution.output_file(f"{volume_out}"),
    )
    execution.run(cargs)
    return ret