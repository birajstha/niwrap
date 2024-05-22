# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


SURFACE_CLOSEST_VERTEX_METADATA = Metadata(
    id="464fdcd54c3d5f63c79bdb5ebe8a0b3efb447891",
    name="surface-closest-vertex",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class SurfaceClosestVertexOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_closest_vertex(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def surface_closest_vertex(
    surface: InputPathType,
    coord_list_file: str,
    vertex_list_out: str,
    runner: Runner = None,
) -> SurfaceClosestVertexOutputs:
    """
    surface-closest-vertex by Washington University School of Medicin.
    
    FIND CLOSEST SURFACE VERTEX TO COORDINATES.
    
    For each coordinate XYZ triple, find the closest vertex in the surface, and
    output its vertex number into a text file. The input file should only use
    whitespace to separate coordinates (spaces, newlines, tabs), for instance:
    
    20 30 25
    30 -20 10.
    
    Args:
        surface: the surface to use
        coord_list_file: text file with coordinates
        vertex_list_out: output - the output text file with vertex numbers
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `SurfaceClosestVertexOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_CLOSEST_VERTEX_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-closest-vertex")
    cargs.append(execution.input_file(surface))
    cargs.append(coord_list_file)
    cargs.append(vertex_list_out)
    ret = SurfaceClosestVertexOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_CLOSEST_VERTEX_METADATA",
    "SurfaceClosestVertexOutputs",
    "surface_closest_vertex",
]