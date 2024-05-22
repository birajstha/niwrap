# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


FSL_ROI_METADATA = Metadata(
    id="5ca25c7a534a575d6ef75dc12ed13d97ec4b0cbc",
    name="FSL roi",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class FslRoiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_roi(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    roi_file_outfile: OutputPathType
    """Output ROI file."""


def fsl_roi(
    in_file: InputPathType,
    roi_file: str,
    t_min: int | None = None,
    t_size: int | None = None,
    x_min: int | None = None,
    x_size: int | None = None,
    y_min: int | None = None,
    y_size: int | None = None,
    z_min: int | None = None,
    z_size: int | None = None,
    runner: Runner = None,
) -> FslRoiOutputs:
    """
    FSL roi by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    Extract region of interest (ROI) from an image.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Fslutils
    
    Args:
        in_file: Input image to extract ROI from.
        roi_file: Output ROI file.
        t_min: Minimum index for t-dimension.
        t_size: Size of ROI in t-dimension.
        x_min: Minimum index for x-dimension.
        x_size: Size of ROI for x-dimension.
        y_min: Minimum index for y-dimension.
        y_size: Size of ROI for y-dimension.
        z_min: Minimum index for z-dimension.
        z_size: Size of ROI for z-dimension.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `FslRoiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_ROI_METADATA)
    cargs = []
    cargs.append("fslroi")
    cargs.append(execution.input_file(in_file))
    cargs.append(roi_file)
    if x_min is not None:
        cargs.append(str(x_min))
    if x_size is not None:
        cargs.append(str(x_size))
    if y_min is not None:
        cargs.append(str(y_min))
    if y_size is not None:
        cargs.append(str(y_size))
    if z_min is not None:
        cargs.append(str(z_min))
    if z_size is not None:
        cargs.append(str(z_size))
    if t_min is not None:
        cargs.append(str(t_min))
    if t_size is not None:
        cargs.append(str(t_size))
    ret = FslRoiOutputs(
        root=execution.output_file("."),
        roi_file_outfile=execution.output_file(f"{roi_file}.nii.gz", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSL_ROI_METADATA",
    "FslRoiOutputs",
    "fsl_roi",
]
