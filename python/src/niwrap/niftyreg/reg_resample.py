# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

REG_RESAMPLE_METADATA = Metadata(
    id="50f0da9e2bc6ab8122fa0747723f0f1cd6f03dbc",
    name="reg_resample",
)


class RegResampleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `reg_resample(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_resampled_image: OutputPathType | None
    """File containing the resampled image"""
    output_resampled_blank: OutputPathType | None
    """File containing the resampled blank grid"""


def reg_resample(
    reference_image: InputPathType,
    floating_image: InputPathType,
    affine_transform: InputPathType | None = None,
    flirt_affine_transform: InputPathType | None = None,
    control_point_grid: InputPathType | None = None,
    deformation_field: InputPathType | None = None,
    resampled_image: str | None = None,
    resampled_blank: str | None = None,
    nearest_neighbor: bool = False,
    linear_interpolation: bool = False,
    runner: Runner = None,
) -> RegResampleOutputs:
    """
    reg_resample by Marc Modat.
    
    Tool for resampling floating images to the reference image space using
    different transformations.
    
    More information: http://cmictig.cs.ucl.ac.uk/wiki/index.php/NiftyReg
    
    Args:
        reference_image: Filename of the reference image.
        floating_image: Filename of the floating image.
        affine_transform: Filename which contains an affine transformation\
            (Affine*Reference=Floating).
        flirt_affine_transform: Filename which contains a radiological flirt\
            affine transformation.
        control_point_grid: Filename of the control point grid image (from\
            reg_f3d).
        deformation_field: Filename of the deformation field image (from\
            reg_transform).
        resampled_image: Filename of the resampled image.
        resampled_blank: Filename of the resampled blank grid.
        nearest_neighbor: Use a Nearest Neighbor interpolation for the source\
            resampling (cubic spline by default).
        linear_interpolation: Use a Linear interpolation for the source\
            resampling (cubic spline by default).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RegResampleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(REG_RESAMPLE_METADATA)
    cargs = []
    cargs.append("reg_resample")
    cargs.extend(["-ref", execution.input_file(reference_image)])
    cargs.extend(["-flo", execution.input_file(floating_image)])
    cargs.append("[TRANSFORMATION_OPTION]")
    cargs.append("[OUTPUT_OPTIONS]")
    cargs.append("[INTERPOLATION_OPTIONS]")
    ret = RegResampleOutputs(
        root=execution.output_file("."),
        output_resampled_image=execution.output_file(f"{resampled_image}", optional=True) if resampled_image is not None else None,
        output_resampled_blank=execution.output_file(f"{resampled_blank}", optional=True) if resampled_blank is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "REG_RESAMPLE_METADATA",
    "RegResampleOutputs",
    "reg_resample",
]
