# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

REG_ALADIN_METADATA = Metadata(
    id="0cdcd5294ca36b2c6f5e68cc4ee34d2019bd8f9f.boutiques",
    name="reg_aladin",
    package="niftyreg",
    container_image_tag="vnmd/niftyreg_1.4.0:20220819",
)


class RegAladinOutputs(typing.NamedTuple):
    """
    Output object returned when calling `reg_aladin(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_affine_file: OutputPathType
    """File containing the output affine transformation"""


def reg_aladin(
    reference_image: InputPathType,
    floating_image: InputPathType,
    symmetric: bool = False,
    output_affine: str | None = None,
    rigid_only: bool = False,
    direct_affine: bool = False,
    smooth_ref: float | None = None,
    smooth_float: float | None = None,
    num_levels: float | None = None,
    first_levels: float | None = None,
    use_nifti_origin: bool = False,
    percent_block: float | None = None,
    percent_inlier: float | None = None,
    runner: Runner | None = None,
) -> RegAladinOutputs:
    """
    Block Matching algorithm for global registration based on "Reconstructing a 3D
    structure from serial histological sections", Image and Vision Computing, 2001.
    
    Author: NiftyReg Developers
    
    URL: http://cmictig.cs.ucl.ac.uk/wiki/index.php/NiftyReg
    
    Args:
        reference_image: Filename of the reference (target) image.
        floating_image: Filename of the floating (source) image.
        symmetric: Uses symmetric version of the algorithm.
        output_affine: Filename which contains the output affine transformation.
        rigid_only: To perform a rigid registration only.
        direct_affine: Directly optimize 12 DoF affine.
        smooth_ref: Smooth the reference image using the specified sigma (mm).
        smooth_float: Smooth the floating image using the specified sigma (mm).
        num_levels: Number of levels to perform.
        first_levels: Only perform the first levels.
        use_nifti_origin: Use the NIFTI header origins to initialize the\
            translation.
        percent_block: Percentage of block to use.
        percent_inlier: Percentage of inlier for the LTS.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RegAladinOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(REG_ALADIN_METADATA)
    cargs = []
    cargs.append("reg_aladin")
    cargs.extend([
        "-ref",
        execution.input_file(reference_image)
    ])
    cargs.extend([
        "-flo",
        execution.input_file(floating_image)
    ])
    if symmetric:
        cargs.append("-sym")
    if output_affine is not None:
        cargs.extend([
            "-aff",
            output_affine
        ])
    if rigid_only:
        cargs.append("-rigOnly")
    if direct_affine:
        cargs.append("-affDirect")
    if smooth_ref is not None:
        cargs.extend([
            "-smooR",
            str(smooth_ref)
        ])
    if smooth_float is not None:
        cargs.extend([
            "-smooF",
            str(smooth_float)
        ])
    if num_levels is not None:
        cargs.extend([
            "-ln",
            str(num_levels)
        ])
    if first_levels is not None:
        cargs.extend([
            "-lp",
            str(first_levels)
        ])
    if use_nifti_origin:
        cargs.append("-nac")
    if percent_block is not None:
        cargs.extend([
            "-%v",
            str(percent_block)
        ])
    if percent_inlier is not None:
        cargs.extend([
            "-%i",
            str(percent_inlier)
        ])
    ret = RegAladinOutputs(
        root=execution.output_file("."),
        output_affine_file=execution.output_file("outputAffine.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "REG_ALADIN_METADATA",
    "RegAladinOutputs",
    "reg_aladin",
]
