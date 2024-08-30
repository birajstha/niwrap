# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_AUTO_TCORRELATE_METADATA = Metadata(
    id="161ed90571de4b91083a0d7c2db4f33bed959f92",
    name="3dAutoTcorrelate",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dAutoTcorrelateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_auto_tcorrelate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_brick: OutputPathType | None
    """Main output dataset"""
    output_head: OutputPathType | None
    """Header information for main output dataset"""
    out1d_file: OutputPathType | None
    """Output in 1D text format"""


def v_3d_auto_tcorrelate(
    input_dataset: InputPathType,
    pearson: bool = False,
    eta2: bool = False,
    polort: int | None = None,
    autoclip: bool = False,
    automask: bool = False,
    mask: InputPathType | None = None,
    mask_only_targets: bool = False,
    mask_source: InputPathType | None = None,
    prefix: str | None = None,
    out1d: str | None = None,
    time_: bool = False,
    mmap_: bool = False,
    runner: Runner | None = None,
) -> V3dAutoTcorrelateOutputs:
    """
    3dAutoTcorrelate by AFNI Team.
    
    Computes the correlation coefficient between the time series of each pair of
    voxels in the input dataset.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dAutoTcorrelate.html
    
    Args:
        input_dataset: Input dataset.
        pearson: Correlation is the normal Pearson (product moment) correlation\
            coefficient [default].
        eta2: Output is eta^2 measure from Cohen et al., NeuroImage, 2008.
        polort: Remove polynomial trend of order 'm', for m=-1..3.
        autoclip: Clip off low-intensity regions in the dataset.
        automask: Apply automask to the dataset.
        mask: Mask of both 'source' and 'target' voxels.
        mask_only_targets: Provide output for all voxels.
        mask_source: Provide output for voxels only in specified mask.
        prefix: Save output into dataset with specified prefix.
        out1d: Save output in a text file in 1D format.
        time_: Mark output as a 3D+time dataset.
        mmap_: Write .BRIK results to disk directly using Unix mmap().
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dAutoTcorrelateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_AUTO_TCORRELATE_METADATA)
    cargs = []
    cargs.append("3dAutoTcorrelate")
    cargs.append("[OPTIONS]")
    cargs.append(execution.input_file(input_dataset))
    ret = V3dAutoTcorrelateOutputs(
        root=execution.output_file("."),
        output_brick=execution.output_file(f"{prefix}.BRIK") if prefix is not None else None,
        output_head=execution.output_file(f"{prefix}.HEAD") if prefix is not None else None,
        out1d_file=execution.output_file(f"{out1d}", optional=True) if out1d is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dAutoTcorrelateOutputs",
    "V_3D_AUTO_TCORRELATE_METADATA",
    "v_3d_auto_tcorrelate",
]