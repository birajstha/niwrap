# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

REG_TOOLS_METADATA = Metadata(
    id="e8762015fe54631608856e6d7449d9e66b9381ef",
    name="reg_tools",
)


class RegToolsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `reg_tools(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image_file: OutputPathType | None
    """File containing the output image"""


def reg_tools(
    input_image: InputPathType,
    output_image: str | None = None,
    add_value_or_image: str | None = None,
    sub_value_or_image: str | None = None,
    mul_value_or_image: str | None = None,
    div_value_or_image: str | None = None,
    smooth_value: float | int | None = None,
    smooth_gaussian: list[float | int] | None = None,
    rms_image: InputPathType | None = None,
    binarize: bool = False,
    threshold_value: float | int | None = None,
    nan_mask_image: InputPathType | None = None,
    runner: Runner | None = None,
) -> RegToolsOutputs:
    """
    reg_tools by Marc Modat.
    
    A versatile tool for manipulating and processing medical images.
    
    More information: http://cmictig.cs.ucl.ac.uk/wiki/index.php/NiftyReg
    
    Args:
        input_image: Filename of the input image.
        output_image: Filename of the output image.
        add_value_or_image: This image (or value) is added to the input.
        sub_value_or_image: This image (or value) is subtracted from the input.
        mul_value_or_image: This image (or value) is multiplied with the input.
        div_value_or_image: This image (or value) is divided by the input.
        smooth_value: The input image is smoothed using a B-spline curve.
        smooth_gaussian: The input image is smoothed using a Gaussian kernel.
        rms_image: Compute the mean RMS between the input image and this image.
        binarize: Binarize the input image (val!=0?val=1:val=0).
        threshold_value: Threshold the input image (val<thr?val=0:val=1).
        nan_mask_image: This image is used to mask the input image. Voxels\
            outside of the mask are set to NaN.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RegToolsOutputs`).
    """
    runner = runner or get_global_runner()
    if smooth_gaussian is not None and (len(smooth_gaussian) != 3): 
        raise ValueError(f"Length of 'smooth_gaussian' must be 3 but was {len(smooth_gaussian)}")
    execution = runner.start_execution(REG_TOOLS_METADATA)
    cargs = []
    cargs.append("reg_tools")
    cargs.extend(["-in", execution.input_file(input_image)])
    if output_image is not None:
        cargs.extend(["-out", output_image])
    cargs.append("[OPTIONS]")
    ret = RegToolsOutputs(
        root=execution.output_file("."),
        output_image_file=execution.output_file(f"{output_image}", optional=True) if output_image is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "REG_TOOLS_METADATA",
    "RegToolsOutputs",
    "reg_tools",
]
