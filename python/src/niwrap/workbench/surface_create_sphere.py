# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SURFACE_CREATE_SPHERE_METADATA = Metadata(
    id="5a9e1fb8066594280699ff24d851560616ea7e07",
    name="surface-create-sphere",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class SurfaceCreateSphereOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_create_sphere(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    sphere_out: OutputPathType
    """the output sphere"""


def surface_create_sphere(
    num_vertices: int,
    sphere_out: str,
    runner: Runner | None = None,
) -> SurfaceCreateSphereOutputs:
    """
    surface-create-sphere by Washington University School of Medicin.
    
    Generate a sphere with consistent vertex areas.
    
    Generates a sphere by regularly dividing the triangles of an icosahedron, to
    come as close to the desired number of vertices as possible, and modifying
    it to have very similar vertex areas for all vertices. To generate a pair of
    vertex-matched left and right spheres, use this command, then
    -surface-flip-lr to generate the other sphere, then -set-structure on each.
    For example:
    
    $ wb_command -surface-create-sphere 6000 Sphere.6k.R.surf.gii
    $ wb_command -surface-flip-lr Sphere.6k.R.surf.gii Sphere.6k.L.surf.gii
    $ wb_command -set-structure Sphere.6k.R.surf.gii CORTEX_RIGHT
    $ wb_command -set-structure Sphere.6k.L.surf.gii CORTEX_LEFT.
    
    Args:
        num_vertices: desired number of vertices.
        sphere_out: the output sphere.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceCreateSphereOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_CREATE_SPHERE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-create-sphere")
    cargs.append(str(num_vertices))
    cargs.append(sphere_out)
    ret = SurfaceCreateSphereOutputs(
        root=execution.output_file("."),
        sphere_out=execution.output_file(f"{sphere_out}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_CREATE_SPHERE_METADATA",
    "SurfaceCreateSphereOutputs",
    "surface_create_sphere",
]
