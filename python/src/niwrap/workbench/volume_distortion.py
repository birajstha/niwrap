# This file was auto generated by Styx.
# Do not edit this file directly.

import pathlib
import typing

from styxdefs import *


VOLUME_DISTORTION_METADATA = Metadata(
    id="f2f4a3fb621316ec40b599b567aef29d92d0674b",
    name="volume-distortion",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class VolumeDistortionOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_distortion(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output distortion measures"""


def volume_distortion(
    warpfield: str,
    volume_out: InputPathType,
    opt_fnirt_source_volume: str | None = None,
    opt_circular: bool = False,
    opt_log2: bool = False,
    runner: Runner = None,
) -> VolumeDistortionOutputs:
    """
    volume-distortion by Washington University School of Medicin.
    
    Calculate volume warpfield distortion.
    
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
        warpfield: the warpfield to compute the distortion of
        volume_out: the output distortion measures
        opt_fnirt_source_volume: MUST be used if using a fnirt warpfield: the
            source volume used when generating the warpfield
        opt_circular: use the circle-based formula for the anisotropic measure
        opt_log2: apply base-2 log transform
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `VolumeDistortionOutputs`).
    """
    runner = runner or get_global_runner()
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
        root=execution.output_file("."),
        volume_out=execution.output_file(f"{pathlib.Path(volume_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_DISTORTION_METADATA",
    "VolumeDistortionOutputs",
    "volume_distortion",
]
