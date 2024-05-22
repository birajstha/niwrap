# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


SURFACE_TO_SURFACE_3D_DISTANCE_METADATA = Metadata(
    id="ea52ef3a19d11965fa3647f3c4e364a8de124429",
    name="surface-to-surface-3d-distance",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class SurfaceToSurface3dDistanceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_to_surface_3d_distance(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    dists_out: OutputPathType
    """the output distances"""


def surface_to_surface_3d_distance(
    surface_comp: InputPathType,
    surface_ref: InputPathType,
    dists_out: InputPathType,
    opt_vectors: bool = False,
    runner: Runner = None,
) -> SurfaceToSurface3dDistanceOutputs:
    """
    surface-to-surface-3d-distance by Washington University School of Medicin.
    
    COMPUTE DISTANCE BETWEEN CORRESPONDING VERTICES.
    
    Computes the vector difference between the vertices of each surface with the
    same index, as (comp - ref), and output the magnitudes, and optionally the
    displacement vectors.
    
    Args:
        surface_comp: the surface to compare to the reference
        surface_ref: the surface to use as the reference
        dists_out: the output distances
        opt_vectors: output the displacement vectors
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `SurfaceToSurface3dDistanceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_TO_SURFACE_3D_DISTANCE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-to-surface-3d-distance")
    cargs.append(execution.input_file(surface_comp))
    cargs.append(execution.input_file(surface_ref))
    cargs.append(execution.input_file(dists_out))
    if opt_vectors:
        cargs.append("-vectors")
    ret = SurfaceToSurface3dDistanceOutputs(
        root=execution.output_file("."),
        dists_out=execution.output_file(f"{pathlib.Path(dists_out).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_TO_SURFACE_3D_DISTANCE_METADATA",
    "SurfaceToSurface3dDistanceOutputs",
    "surface_to_surface_3d_distance",
]
