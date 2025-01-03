# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURFACE_INFORMATION_METADATA = Metadata(
    id="757610425a8d086526ce21babe9d148126110db0.boutiques",
    name="surface-information",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


class SurfaceInformationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_information(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def surface_information(
    surface_file: InputPathType,
    runner: Runner | None = None,
) -> SurfaceInformationOutputs:
    """
    Display information about a surface.
    
    Information about surface is displayed including vertices,
    triangles, bounding box, and spacing.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        surface_file: Surface for which information is displayed.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceInformationOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_INFORMATION_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-information")
    cargs.append(execution.input_file(surface_file))
    ret = SurfaceInformationOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_INFORMATION_METADATA",
    "SurfaceInformationOutputs",
    "surface_information",
]
