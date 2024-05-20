# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


SURFACE_MODIFY_SPHERE_METADATA = Metadata(
    id="2bc79d9fa7ac597b349f44349e56a15b7594b22c",
    name="surface-modify-sphere",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class SurfaceModifySphereOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_modify_sphere(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    sphere_out: OutputPathType
    """the output sphere"""


def surface_modify_sphere(
    runner: Runner,
    sphere_in: InputPathType,
    radius: float | int,
    sphere_out: InputPathType,
    opt_recenter: bool = False,
) -> SurfaceModifySphereOutputs:
    """
    CHANGE RADIUS AND OPTIONALLY RECENTER A SPHERE.
    
    This command may be useful if you have used -surface-resample to resample a
    sphere, which can suffer from problems generally not present in
    -surface-sphere-project-unproject. If the sphere should already be centered
    around the origin, using -recenter may still shift it slightly before
    changing the radius, which is likely to be undesireable.
    
    If <sphere-in> is not close to spherical, or not centered around the origin
    and -recenter is not used, a warning is printed.
    
    Args:
        runner: Command runner
        sphere_in: the sphere to modify
        radius: the radius the output sphere should have
        sphere_out: the output sphere
        opt_recenter: recenter the sphere by means of the bounding box
    Returns:
        NamedTuple of outputs (described in `SurfaceModifySphereOutputs`).
    """
    execution = runner.start_execution(SURFACE_MODIFY_SPHERE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-modify-sphere")
    cargs.append(execution.input_file(sphere_in))
    cargs.append(str(radius))
    cargs.append(execution.input_file(sphere_out))
    if opt_recenter:
        cargs.append("-recenter")
    ret = SurfaceModifySphereOutputs(
        root=execution.output_file("."),
        sphere_out=execution.output_file(f"{pathlib.Path(sphere_out).stem}"),
    )
    execution.run(cargs)
    return ret
