# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_PVMAP_METADATA = Metadata(
    id="55dba5084ade4c336efba69e81addccf3e2d93a3.boutiques",
    name="3dPVmap",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dPvmapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_pvmap(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outbrik: OutputPathType | None
    """Output PVmap file"""
    outhead: OutputPathType | None
    """Output PVmap header file"""
    pc_vectors: OutputPathType | None
    """Principal component time series vectors"""


def v_3d_pvmap(
    inputdataset: InputPathType,
    prefix: str | None = None,
    mask: InputPathType | None = None,
    automask: bool = False,
    runner: Runner | None = None,
) -> V3dPvmapOutputs:
    """
    Computes the first two principal component vectors of a time series dataset,
    then outputs the R-squared coefficient of each voxel time series with these
    first two components.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        inputdataset: Input dataset (e.g., fred.nii).
        prefix: Output prefix for generated files.
        mask: Mask dataset (e.g., brainmask.nii).
        automask: Automatically generate a mask from the input dataset.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dPvmapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_PVMAP_METADATA)
    cargs = []
    cargs.append("3dPVmap")
    if prefix is not None:
        cargs.extend([
            "-prefix",
            prefix
        ])
    if mask is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask)
        ])
    if automask:
        cargs.append("-automask")
    cargs.append(execution.input_file(inputdataset))
    ret = V3dPvmapOutputs(
        root=execution.output_file("."),
        outbrik=execution.output_file(prefix + "+orig.BRIK") if (prefix is not None) else None,
        outhead=execution.output_file(prefix + "+orig.HEAD") if (prefix is not None) else None,
        pc_vectors=execution.output_file(prefix + ".1D") if (prefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dPvmapOutputs",
    "V_3D_PVMAP_METADATA",
    "v_3d_pvmap",
]
