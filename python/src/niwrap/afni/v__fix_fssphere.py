# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V__FIX_FSSPHERE_METADATA = Metadata(
    id="22439f8b6f8027a3d078c6f8e58e5eb187e31050",
    name="@fix_FSsphere",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class VFixFssphereOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__fix_fssphere(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    corrected_surface: OutputPathType
    """Corrected surface"""


def v__fix_fssphere(
    spec_file: InputPathType,
    sphere_file: InputPathType,
    num_iterations: int | None = None,
    extent_lim: float | int | None = None,
    project_first: bool = False,
    keep_temp: bool = False,
    runner: Runner | None = None,
) -> VFixFssphereOutputs:
    """
    @fix_FSsphere by AFNI Team.
    
    Tool for fixing errors in FreeSurfer spherical surfaces.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@fix_FSsphere.html
    
    Args:
        spec_file: Spec file.
        sphere_file: SPHERE.asc is the sphere to be used.
        num_iterations: Number of local smoothing operations. Default is 3000.
        extent_lim: Extent, in mm, by which troubled sections are fattened.\
            Default is 6.
        project_first: Project to a sphere, before smoothing. Default is 0.
        keep_temp: Keep temporary files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VFixFssphereOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__FIX_FSSPHERE_METADATA)
    cargs = []
    cargs.append("@fix_FSsphere")
    cargs.append("<-spec")
    cargs.append("SPEC>")
    cargs.append("<-sphere")
    cargs.append("SPHERE.asc>")
    cargs.append("[-niter")
    cargs.append("NITER]")
    cargs.append("[-lim")
    cargs.append("LIM]")
    cargs.append("[-keep_temp]")
    cargs.append("[-project_first]")
    ret = VFixFssphereOutputs(
        root=execution.output_file("."),
        corrected_surface=execution.output_file(f"[SPHERE]_fxd.asc"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VFixFssphereOutputs",
    "V__FIX_FSSPHERE_METADATA",
    "v__fix_fssphere",
]