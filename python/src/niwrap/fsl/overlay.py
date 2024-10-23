# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

OVERLAY_METADATA = Metadata(
    id="aece53ed3600407081126a33435263f96938ce16.boutiques",
    name="overlay",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class OverlayOutputs(typing.NamedTuple):
    """
    Output object returned when calling `overlay(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file_outfile: OutputPathType | None
    """Combined image volume."""


def overlay(
    background_image: InputPathType,
    bg_thresh: list[float],
    stat_image: InputPathType,
    stat_thresh: list[float],
    auto_thresh_bg: bool = False,
    full_bg_range: bool = False,
    out_file: InputPathType | None = None,
    out_type: typing.Literal["float", "int"] | None = "float",
    output_type: typing.Literal["NIFTI", "NIFTI_PAIR", "NIFTI_GZ", "NIFTI_PAIR_GZ"] | None = None,
    stat_image2: InputPathType | None = None,
    stat_thresh2: list[float] | None = None,
    use_checkerboard: bool = False,
    runner: Runner | None = None,
) -> OverlayOutputs:
    """
    Use FSL's overlay command to combine background and statistical images into one
    volume.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        background_image: Image to use as background.
        bg_thresh: (a float, a float). Min and max values for background\
            intensity.
        stat_image: Statistical image to overlay in color.
        stat_thresh: (a float, a float). Min and max values for the statistical\
            overlay.
        auto_thresh_bg: Automatically threshold the background image.
        full_bg_range: Use full range of background image.
        out_file: Combined image volume.
        out_type: 'float' or 'int'. Write output with float or int.
        output_type: 'nifti' or 'nifti_pair' or 'nifti_gz' or 'nifti_pair_gz'.\
            Fsl output type.
        stat_image2: Second statistical image to overlay in color.
        stat_thresh2: (a float, a float). Min and max values for second\
            statistical overlay.
        use_checkerboard: Use checkerboard mask for overlay.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `OverlayOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(OVERLAY_METADATA)
    cargs = []
    cargs.append("overlay")
    if auto_thresh_bg:
        cargs.append("-a")
    cargs.append(execution.input_file(background_image))
    cargs.extend(map(str, bg_thresh))
    if full_bg_range:
        cargs.append("-A")
    if out_file is not None:
        cargs.append(execution.input_file(out_file))
    if out_type is not None:
        cargs.append(out_type)
    if output_type is not None:
        cargs.append(output_type)
    cargs.append(execution.input_file(stat_image))
    if stat_image2 is not None:
        cargs.append(execution.input_file(stat_image2))
    cargs.extend(map(str, stat_thresh))
    if stat_thresh2 is not None:
        cargs.extend(map(str, stat_thresh2))
    if use_checkerboard:
        cargs.append("-c")
    ret = OverlayOutputs(
        root=execution.output_file("."),
        out_file_outfile=execution.output_file(pathlib.Path(out_file).name) if (out_file is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "OVERLAY_METADATA",
    "OverlayOutputs",
    "overlay",
]
