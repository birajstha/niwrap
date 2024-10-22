# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURFACE_SMOOTHING_METADATA = Metadata(
    id="c1bedfe431bf5011c8cb46f37e166893c8350088.boutiques",
    name="surface-smoothing",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


class SurfaceSmoothingOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_smoothing(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    surface_out: OutputPathType
    """output surface file"""


def surface_smoothing(
    surface_in: InputPathType,
    smoothing_strength: float,
    smoothing_iterations: int,
    surface_out: str,
    runner: Runner | None = None,
) -> SurfaceSmoothingOutputs:
    """
    Surface smoothing.
    
    Smooths a surface by averaging vertex coordinates with those of the
    neighboring vertices.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        surface_in: the surface file to smooth.
        smoothing_strength: smoothing strength (ranges [0.0 - 1.0]).
        smoothing_iterations: smoothing iterations.
        surface_out: output surface file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceSmoothingOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_SMOOTHING_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-smoothing")
    cargs.append(execution.input_file(surface_in))
    cargs.append(str(smoothing_strength))
    cargs.append(str(smoothing_iterations))
    cargs.append(surface_out)
    ret = SurfaceSmoothingOutputs(
        root=execution.output_file("."),
        surface_out=execution.output_file(surface_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_SMOOTHING_METADATA",
    "SurfaceSmoothingOutputs",
    "surface_smoothing",
]
