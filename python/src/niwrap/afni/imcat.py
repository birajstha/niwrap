# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

IMCAT_METADATA = Metadata(
    id="aaf3852ed2e5487ca6e742c661a53a14976a9a76.boutiques",
    name="imcat",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class ImcatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `imcat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image_file: OutputPathType | None
    """Output image file"""


def imcat(
    input_files: list[InputPathType],
    scale_image: InputPathType | None = None,
    scale_pixels: InputPathType | None = None,
    scale_intensity: bool = False,
    gscale: float | None = None,
    rgb_out: bool = False,
    res_in: list[float] | None = None,
    respad_in: list[float] | None = None,
    pad_val: float | None = None,
    crop: list[float] | None = None,
    autocrop_ctol: float | None = None,
    autocrop_atol: float | None = None,
    autocrop: bool = False,
    zero_wrap: bool = False,
    white_wrap: bool = False,
    gray_wrap: float | None = None,
    image_wrap: bool = False,
    rand_wrap: bool = False,
    prefix: str | None = None,
    matrix: list[float] | None = None,
    nx: float | None = None,
    ny: float | None = None,
    matrix_from_scale: bool = False,
    gap: float | None = None,
    gap_col: list[float] | None = None,
    runner: Runner | None = None,
) -> ImcatOutputs:
    """
    Assembles a set of images into an image matrix (IM) montage of NX by NY images.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_files: Input image files.
        scale_image: Multiply each image IM(i,j) in output image matrix IM by\
            the color or intensity of the pixel (i,j) in SCALE_IMG.
        scale_pixels: Multiply each pixel (i,j) in output image by the color or\
            intensity of the pixel (i,j) in SCALE_IMG. SCALE_IMG is automatically\
            resized to the resolution of the output image.
        scale_intensity: Instead of multiplying by the color of pixel (i,j),\
            use its intensity (average color).
        gscale: Apply FAC in addition to scaling of -scale_* options.
        rgb_out: Force output to be in RGB, even if input is bytes. This option\
            is turned on automatically in certain cases.
        res_in: Set resolution of all input images to RX by RY pixels. Default\
            is to make all input have the same resolution as the first image.
        respad_in: Like -res_in, but resample to the max while respecting the\
            aspect ratio, and then pad to achieve desired pixel count.
        pad_val: Set the padding value, should it be needed by -respad_in to\
            VAL. VAL is typecast to byte, default is 0, max is 255.
        crop: Crop images by L (Left), R (Right), T (Top), B (Bottom) pixels.\
            Cutting is performed after any resolution change, if any, is to be\
            done.
        autocrop_ctol: A line is eliminated if none of its R G B values differ\
            by more than CTOL% from those of the corner pixel.
        autocrop_atol: A line is eliminated if none of its R G B values differ\
            by more than ATOL% from those of line average.
        autocrop: This option is the same as using both of -autocrop_atol 20\
            and -autocrop_ctol 20.
        zero_wrap: If number of images is not enough to fill matrix solid black\
            images are used.
        white_wrap: If number of images is not enough to fill matrix solid\
            white images are used.
        gray_wrap: If number of images is not enough to fill matrix, solid gray\
            images are used. GRAY must be between 0 and 1.0.
        image_wrap: If number of images is not enough to fill matrix, images on\
            command line are reused (default).
        rand_wrap: When reusing images to fill matrix, randomize the order in\
            refill section only.
        prefix: Prefix the output files with string 'ppp'.
        matrix: Specify number of images in each row and column of IM at the\
            same time.
        nx: Number of images in each row.
        ny: Number of images in each column.
        matrix_from_scale: Set NX and NY to be the same as the SCALE_IMG's\
            dimensions. (needs -scale_image).
        gap: Put a line G pixels wide between images.
        gap_col: Set color of line to R G B values. Values range between 0 and\
            255.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ImcatOutputs`).
    """
    if pad_val is not None and not (0 <= pad_val <= 255): 
        raise ValueError(f"'pad_val' must be between 0 <= x <= 255 but was {pad_val}")
    if gray_wrap is not None and not (0.0 <= gray_wrap <= 1.0): 
        raise ValueError(f"'gray_wrap' must be between 0.0 <= x <= 1.0 but was {gray_wrap}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(IMCAT_METADATA)
    cargs = []
    cargs.append("imcat")
    cargs.extend([execution.input_file(f) for f in input_files])
    if scale_image is not None:
        cargs.extend([
            "-scale_image",
            execution.input_file(scale_image)
        ])
    if scale_pixels is not None:
        cargs.extend([
            "-scale_pixels",
            execution.input_file(scale_pixels)
        ])
    if scale_intensity:
        cargs.append("-scale_intensity")
    if gscale is not None:
        cargs.extend([
            "-gscale",
            str(gscale)
        ])
    if rgb_out:
        cargs.append("-rgb_out")
    if res_in is not None:
        cargs.extend([
            "-res_in",
            *map(str, res_in)
        ])
    if respad_in is not None:
        cargs.extend([
            "-respad_in",
            *map(str, respad_in)
        ])
    if pad_val is not None:
        cargs.extend([
            "-pad_val",
            str(pad_val)
        ])
    if crop is not None:
        cargs.extend([
            "-crop",
            *map(str, crop)
        ])
    if autocrop_ctol is not None:
        cargs.extend([
            "-autocrop_ctol",
            str(autocrop_ctol)
        ])
    if autocrop_atol is not None:
        cargs.extend([
            "-autocrop_atol",
            str(autocrop_atol)
        ])
    if autocrop:
        cargs.append("-autocrop")
    if zero_wrap:
        cargs.append("-zero_wrap")
    if white_wrap:
        cargs.append("-white_wrap")
    if gray_wrap is not None:
        cargs.extend([
            "-gray_wrap",
            str(gray_wrap)
        ])
    if image_wrap:
        cargs.append("-image_wrap")
    if rand_wrap:
        cargs.append("-rand_wrap")
    if prefix is not None:
        cargs.extend([
            "-prefix",
            prefix
        ])
    if matrix is not None:
        cargs.extend([
            "-matrix",
            *map(str, matrix)
        ])
    if nx is not None:
        cargs.extend([
            "-nx",
            str(nx)
        ])
    if ny is not None:
        cargs.extend([
            "-ny",
            str(ny)
        ])
    if matrix_from_scale:
        cargs.append("-matrix_from_scale")
    if gap is not None:
        cargs.extend([
            "-gap",
            str(gap)
        ])
    if gap_col is not None:
        cargs.extend([
            "-gap_col",
            *map(str, gap_col)
        ])
    ret = ImcatOutputs(
        root=execution.output_file("."),
        output_image_file=execution.output_file(prefix + "output_image.[EXT]") if (prefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "IMCAT_METADATA",
    "ImcatOutputs",
    "imcat",
]
