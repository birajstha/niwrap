# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SURF_RETINO_MAP_METADATA = Metadata(
    id="ec1b0e191b03919f3ab0af64d9930a48ec7ddd78",
    name="SurfRetinoMap",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class SurfRetinoMapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surf_retino_map(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    vfr_output: OutputPathType | None
    """Output Visual Field Ratio (VFR) dataset."""
    threshold_max_output: OutputPathType | None
    """Maximum threshold at each node in the input datasets."""


def surf_retino_map(
    surface: str,
    polar: str,
    eccentricity: str,
    prefix: str | None = None,
    node_debug: float | int | None = None,
    runner: Runner | None = None,
) -> SurfRetinoMapOutputs:
    """
    SurfRetinoMap by AFNI Team.
    
    Tool for retinotopic mapping on cortical surfaces.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/SurfRetinoMap.html
    
    Args:
        surface: Surface on which distances are computed. See 'Specifying input\
            surfaces' section for syntax.
        polar: Retinotopic dataset: polar angle dataset.
        eccentricity: Retinotopic dataset: eccentricity angle dataset.
        prefix: Prefix for output datasets.
        node_debug: Index of node number for which debugging information is\
            output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfRetinoMapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURF_RETINO_MAP_METADATA)
    cargs = []
    cargs.append("SurfRetinoMap")
    cargs.append(surface)
    cargs.append("-input")
    cargs.append(polar)
    cargs.append(eccentricity)
    cargs.append("[--prefix")
    cargs.append("PREFIX]")
    cargs.append("[--node_dbg")
    cargs.append("NODE]")
    ret = SurfRetinoMapOutputs(
        root=execution.output_file("."),
        vfr_output=execution.output_file(f"{prefix}_VFR.nii.gz", optional=True) if prefix is not None else None,
        threshold_max_output=execution.output_file(f"{prefix}_threshold_max.nii.gz", optional=True) if prefix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURF_RETINO_MAP_METADATA",
    "SurfRetinoMapOutputs",
    "surf_retino_map",
]
