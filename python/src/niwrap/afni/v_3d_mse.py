# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_MSE_METADATA = Metadata(
    id="ff2e9633405885aec7920f250dba5893cb5b6dda.boutiques",
    name="3dMSE",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dMseOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_mse(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_brik: OutputPathType | None
    """Output dataset in BRIK format."""
    out_head: OutputPathType | None
    """Output dataset in HEAD format."""


def v_3d_mse(
    dset: InputPathType,
    polynomial_order: int | None = None,
    autoclip: bool = False,
    automask: bool = False,
    mask: InputPathType | None = None,
    prefix: str | None = None,
    scales: float | None = None,
    entwin: float | None = None,
    rthresh: float | None = None,
    runner: Runner | None = None,
) -> V3dMseOutputs:
    """
    Computes voxelwise multi-scale entropy.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dset: Input dataset (e.g., dset.nii.gz).
        polynomial_order: Remove polynomial trend of order 'm' (default is m=1;\
            m=-1 means no detrending).
        autoclip: Clip off low-intensity regions in the dataset.
        automask: Use automask to clip low-intensity regions.
        mask: Mask to define 'in-brain' voxels.
        prefix: Prefix for the output dataset (default is 'MSE').
        scales: The number of scales to be used in the calculation (default is\
            5).
        entwin: The window size used in the calculation (default is 2).
        rthresh: The radius threshold for determining if values are the same in\
            the SampleEn calculation, in fractions of the standard deviation\
            (default is 0.5).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dMseOutputs`).
    """
    if polynomial_order is not None and not (-1 <= polynomial_order <= 3): 
        raise ValueError(f"'polynomial_order' must be between -1 <= x <= 3 but was {polynomial_order}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_MSE_METADATA)
    cargs = []
    cargs.append("3dMSE")
    if polynomial_order is not None:
        cargs.extend([
            "-polort",
            str(polynomial_order)
        ])
    if autoclip:
        cargs.append("-autoclip")
    if automask:
        cargs.append("-automask")
    if mask is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask)
        ])
    if prefix is not None:
        cargs.extend([
            "-prefix",
            prefix
        ])
    if scales is not None:
        cargs.extend([
            "-scales",
            str(scales)
        ])
    if entwin is not None:
        cargs.extend([
            "-entwin",
            str(entwin)
        ])
    if rthresh is not None:
        cargs.extend([
            "-rthresh",
            str(rthresh)
        ])
    cargs.append(execution.input_file(dset))
    ret = V3dMseOutputs(
        root=execution.output_file("."),
        out_brik=execution.output_file(prefix + "+orig.BRIK") if (prefix is not None) else None,
        out_head=execution.output_file(prefix + "+orig.HEAD") if (prefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dMseOutputs",
    "V_3D_MSE_METADATA",
    "v_3d_mse",
]
