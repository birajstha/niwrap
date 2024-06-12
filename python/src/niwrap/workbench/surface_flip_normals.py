# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SURFACE_FLIP_NORMALS_METADATA = Metadata(
    id="42964755965df68270ab6416523dec60defbd12f",
    name="surface-flip-normals",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class SurfaceFlipNormalsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_flip_normals(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    surface_out: OutputPathType
    """the output surface"""


def surface_flip_normals(
    surface: InputPathType,
    surface_out: InputPathType,
    runner: Runner = None,
) -> SurfaceFlipNormalsOutputs:
    """
    surface-flip-normals by Washington University School of Medicin.
    
    Flip all tiles on a surface.
    
    Flips all triangles on a surface, resulting in surface normals being flipped
    the other direction (inward vs outward). If you transform a surface with an
    affine that has negative determinant, or a warpfield that similarly flips
    the surface, you may end up with a surface that has normals pointing
    inwards, which may have display problems. Using this command will solve that
    problem.
    
    Args:
        surface: the surface to flip the normals of.
        surface_out: the output surface.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceFlipNormalsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_FLIP_NORMALS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-flip-normals")
    cargs.append(execution.input_file(surface))
    cargs.append(execution.input_file(surface_out))
    ret = SurfaceFlipNormalsOutputs(
        root=execution.output_file("."),
        surface_out=execution.output_file(f"{pathlib.Path(surface_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_FLIP_NORMALS_METADATA",
    "SurfaceFlipNormalsOutputs",
    "surface_flip_normals",
]
