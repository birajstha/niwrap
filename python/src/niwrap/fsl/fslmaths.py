# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FSLMATHS_METADATA = Metadata(
    id="73629885021013151882a1808965dcd626886587",
    name="fslmaths",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class FslmathsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslmaths(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Output image"""


def fslmaths(
    infile: InputPathType,
    datatype: str | None = None,
    output_datatype: str | None = None,
    add_operation: str | None = None,
    sub_operation: str | None = None,
    mul_operation: str | None = None,
    div_operation: str | None = None,
    rem_operation: str | None = None,
    mas_operation: InputPathType | None = None,
    thr_operation: float | int | None = None,
    thrp_operation: float | int | None = None,
    uthr_operation: float | int | None = None,
    uthrp_operation: float | int | None = None,
    max_operation: str | None = None,
    min_operation: str | None = None,
    exp_operation: bool = False,
    log_operation: bool = False,
    sin_operation: bool = False,
    cos_operation: bool = False,
    tan_operation: bool = False,
    sqr_operation: bool = False,
    sqrt_operation: bool = False,
    runner: Runner | None = None,
) -> FslmathsOutputs:
    """
    fslmaths by FMRIB Analysis Group, Oxford University, UK.
    
    General command for mathematical manipulation of image intensities and
    generation of statistical data from given images.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Fslutils
    
    Args:
        infile: Input image.
        datatype: Set the datatype used internally for calculations (default\
            float for all except double images).
        output_datatype: Set the output datatype (default is float).
        add_operation: Add following input to current image.
        sub_operation: Subtract following input from current image.
        mul_operation: Multiply current image by following input.
        div_operation: Divide current image by following input.
        rem_operation: Modulus remainder - divide current image by following\
            input and take remainder.
        mas_operation: Use (following image>0) to mask current image.
        thr_operation: Use following number to threshold current image (zero\
            anything below the number).
        thrp_operation: Use following percentage (0-100) of ROBUST RANGE to\
            threshold current image (zero anything below the number).
        uthr_operation: Use following number to upper-threshold current image\
            (zero anything above the number).
        uthrp_operation: Use following percentage (0-100) of ROBUST RANGE to\
            upper-threshold current image (zero anything above the number).
        max_operation: Take maximum of following input and current image.
        min_operation: Take minimum of following input and current image.
        exp_operation: Exponential.
        log_operation: Natural logarithm.
        sin_operation: Sine function.
        cos_operation: Cosine function.
        tan_operation: Tangent function.
        sqr_operation: Square.
        sqrt_operation: Square root.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslmathsOutputs`).
    """
    runner = runner or get_global_runner()
    if thrp_operation is not None and not (0 <= thrp_operation <= 100): 
        raise ValueError(f"'thrp_operation' must be between 0 <= x <= 100 but was {thrp_operation}")
    if uthrp_operation is not None and not (0 <= uthrp_operation <= 100): 
        raise ValueError(f"'uthrp_operation' must be between 0 <= x <= 100 but was {uthrp_operation}")
    execution = runner.start_execution(FSLMATHS_METADATA)
    cargs = []
    cargs.append("fslmaths")
    cargs.append(execution.input_file(infile))
    cargs.append("[OPERATIONS]")
    cargs.append("[OUTPUT_FILE]")
    ret = FslmathsOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(f"[OUTPUT_FILE]"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLMATHS_METADATA",
    "FslmathsOutputs",
    "fslmaths",
]
