# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


SURFACE_SET_COORDINATES_METADATA = Metadata(
    id="2cc070f285b495aef313e7b20fe925a091e86162",
    name="surface-set-coordinates",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class SurfaceSetCoordinatesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_set_coordinates(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    surface_out: OutputPathType
    """the new surface"""


def surface_set_coordinates(
    runner: Runner,
    surface_in: InputPathType,
    coord_metric: InputPathType,
    surface_out: InputPathType,
) -> SurfaceSetCoordinatesOutputs:
    """
    MODIFY COORDINATES OF A SURFACE.
    
    Takes the topology from an existing surface file, and uses values from a
    metric file as coordinates to construct a new surface file.
    
    See -surface-coordinates-to-metric for how to get surface coordinates as a
    metric file, such that you can then modify them via metric commands, etc.
    
    Args:
        runner: Command runner
        surface_in: the surface to use for the topology
        coord_metric: the new coordinates, as a 3-column metric file
        surface_out: the new surface
    Returns:
        NamedTuple of outputs (described in `SurfaceSetCoordinatesOutputs`).
    """
    execution = runner.start_execution(SURFACE_SET_COORDINATES_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-set-coordinates")
    cargs.append(execution.input_file(surface_in))
    cargs.append(execution.input_file(coord_metric))
    cargs.append(execution.input_file(surface_out))
    ret = SurfaceSetCoordinatesOutputs(
        root=execution.output_file("."),
        surface_out=execution.output_file(f"{pathlib.Path(surface_out).stem}"),
    )
    execution.run(cargs)
    return ret
