# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_WINSOR_METADATA = Metadata(
    id="074695a74f3c85c4333be4a448275c193336df53",
    name="3dWinsor",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dWinsorOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_winsor(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile_head: OutputPathType | None
    """Output dataset with Winsorizing filter applied."""
    outfile_brik: OutputPathType | None
    """Output dataset with Winsorizing filter applied."""


def v_3d_winsor(
    dataset: InputPathType,
    irad: float | int | None = None,
    cbot: float | int | None = None,
    ctop: float | int | None = None,
    nrep: float | int | None = None,
    keepzero: bool = False,
    clip: float | int | None = None,
    prefix: str | None = None,
    mask: InputPathType | None = None,
    runner: Runner | None = None,
) -> V3dWinsorOutputs:
    """
    3dWinsor by AFNI Team.
    
    Apply a 3D 'Winsorizing' filter to a short-valued dataset.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dWinsor.html
    
    Args:
        dataset: Input dataset to apply the filter on.
        irad: Include all points within 'distance' rr in the operation, where\
            distance is defined as sqrt(i*i+j*j+k*k), and (i,j,k) are voxel index\
            offsets.
        cbot: Set bottom clip index to bb.
        ctop: Set top clip index to tt.
        nrep: Repeat filter nn times. If nn < 0, means to repeat filter until\
            less than abs(n) voxels change.
        keepzero: Don't filter voxels that are zero.
        clip: Set voxels at or below 'xx' to zero.
        prefix: Use 'pp' as the prefix for the output dataset.
        mask: Use 'mmm' as a mask dataset - voxels NOT in the mask won't be\
            filtered.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dWinsorOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_WINSOR_METADATA)
    cargs = []
    cargs.append("3dWinsor")
    if irad is not None:
        cargs.extend(["-irad", str(irad)])
    if cbot is not None:
        cargs.extend(["-cbot", str(cbot)])
    if ctop is not None:
        cargs.extend(["-ctop", str(ctop)])
    if nrep is not None:
        cargs.extend(["-nrep", str(nrep)])
    if keepzero:
        cargs.append("-keepzero")
    if clip is not None:
        cargs.extend(["-clip", str(clip)])
    if prefix is not None:
        cargs.extend(["-prefix", prefix])
    if mask is not None:
        cargs.extend(["-mask", execution.input_file(mask)])
    cargs.append(execution.input_file(dataset))
    ret = V3dWinsorOutputs(
        root=execution.output_file("."),
        outfile_head=execution.output_file(f"{prefix}+*.HEAD") if prefix is not None else None,
        outfile_brik=execution.output_file(f"{prefix}+*.BRIK") if prefix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dWinsorOutputs",
    "V_3D_WINSOR_METADATA",
    "v_3d_winsor",
]