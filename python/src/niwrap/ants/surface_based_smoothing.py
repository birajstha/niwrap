# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURFACE_BASED_SMOOTHING_METADATA = Metadata(
    id="54b2f342b78002c8629051dfa51b4241d2aa0f9b.boutiques",
    name="SurfaceBasedSmoothing",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


class SurfaceBasedSmoothingOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_based_smoothing(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    smoothed_output: OutputPathType
    """The output smoothed image."""


def surface_based_smoothing(
    image_to_smooth: InputPathType,
    sigma: float,
    surface_image: InputPathType,
    outname: str,
    num_repeats: int | None = None,
    runner: Runner | None = None,
) -> SurfaceBasedSmoothingOutputs:
    """
    Surface-based smoothing applied to ImageToSmooth using a geodesic neighbourhood
    defined by sigma and the surface image.
    
    Author: ANTs developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        image_to_smooth: The image that needs to be smoothed.
        sigma: Geodesic neighborhood radius.
        surface_image: Assumes a label == 1 that defines the surface.
        outname: The name of the output file.
        num_repeats: Number of times the geodesic neighborhood is applied\
            repeatedly.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceBasedSmoothingOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_BASED_SMOOTHING_METADATA)
    cargs = []
    cargs.append("SurfaceBasedSmoothing")
    cargs.append(execution.input_file(image_to_smooth))
    cargs.append(str(sigma))
    cargs.append(execution.input_file(surface_image))
    cargs.append(outname)
    if num_repeats is not None:
        cargs.append(str(num_repeats))
    ret = SurfaceBasedSmoothingOutputs(
        root=execution.output_file("."),
        smoothed_output=execution.output_file(outname),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_BASED_SMOOTHING_METADATA",
    "SurfaceBasedSmoothingOutputs",
    "surface_based_smoothing",
]
