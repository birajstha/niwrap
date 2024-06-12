# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SURFACE_FLIP_LR_METADATA = Metadata(
    id="bd4b1d987f55accd41c674badcf89e23350ec215",
    name="surface-flip-lr",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class SurfaceFlipLrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_flip_lr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    surface_out: OutputPathType
    """the output flipped surface"""


def surface_flip_lr(
    surface: InputPathType,
    surface_out: InputPathType,
    runner: Runner = None,
) -> SurfaceFlipLrOutputs:
    """
    surface-flip-lr by Washington University School of Medicin.
    
    Mirror a surface through the yz plane.
    
    This command negates the x coordinate of each vertex, and flips the surface
    normals, so that you have a surface of opposite handedness with the same
    features and vertex correspondence, with normals consistent with the
    original surface. That is, if the input surface has normals facing outward,
    the output surface will also have normals facing outward.
    
    Args:
        surface: the surface to flip.
        surface_out: the output flipped surface.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceFlipLrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_FLIP_LR_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-flip-lr")
    cargs.append(execution.input_file(surface))
    cargs.append(execution.input_file(surface_out))
    ret = SurfaceFlipLrOutputs(
        root=execution.output_file("."),
        surface_out=execution.output_file(f"{pathlib.Path(surface_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_FLIP_LR_METADATA",
    "SurfaceFlipLrOutputs",
    "surface_flip_lr",
]
