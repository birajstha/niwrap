# This file was auto generated by Styx.
# Do not edit this file directly.

import pathlib
import typing

from styxdefs import *


SURFACE_SPHERE_TRIANGULAR_PATCHES_METADATA = Metadata(
    id="caeaed530c7c13609bae383f92440d35ff909ef0",
    name="surface-sphere-triangular-patches",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class SurfaceSphereTriangularPatchesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_sphere_triangular_patches(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def surface_sphere_triangular_patches(
    sphere: InputPathType,
    divisions: int,
    text_out: str,
    runner: Runner = None,
) -> SurfaceSphereTriangularPatchesOutputs:
    """
    surface-sphere-triangular-patches by Washington University School of Medicin.
    
    Divide standard sphere into patches.
    
    Divide the given undistorted sphere into equally-sized triangular patches.
    Patches overlap by a border of 1 vertex.
    
    Args:
        sphere: an undistorted, regularly divided icosahedral sphere
        divisions: how many pieces to divide each icosahedral edge into, must
            divide perfectly into the given sphere
        text_out: output - text file for the vertex numbers of the patches
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `SurfaceSphereTriangularPatchesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_SPHERE_TRIANGULAR_PATCHES_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-sphere-triangular-patches")
    cargs.append(execution.input_file(sphere))
    cargs.append(str(divisions))
    cargs.append(text_out)
    ret = SurfaceSphereTriangularPatchesOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_SPHERE_TRIANGULAR_PATCHES_METADATA",
    "SurfaceSphereTriangularPatchesOutputs",
    "surface_sphere_triangular_patches",
]
