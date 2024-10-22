# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_AFNITO_RAW_METADATA = Metadata(
    id="67bff5ed68a691d8da5e7aa97ecf946e7772101e.boutiques",
    name="3dAFNItoRaw",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dAfnitoRawOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_afnito_raw(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_3d_afnito_raw(
    dataset: str,
    output_file: str | None = None,
    force_float: bool = False,
    runner: Runner | None = None,
) -> V3dAfnitoRawOutputs:
    """
    Convert an AFNI brik file with multiple sub-briks to a raw file with each
    sub-brik voxel concatenated voxel-wise.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dataset: Input AFNI dataset with possible modifiers for sub-brick and\
            sub-range selection.
        output_file: Name of the output file (not an AFNI dataset prefix).\
            Default is rawxyz.dat.
        force_float: Force floating point output. Floating point forced if any\
            sub-brik scale factors not equal to 1.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dAfnitoRawOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_AFNITO_RAW_METADATA)
    cargs = []
    cargs.append("3dAFNItoRaw")
    if output_file is not None:
        cargs.extend([
            "-output",
            output_file
        ])
    if force_float:
        cargs.append("-datum float")
    cargs.append(dataset)
    ret = V3dAfnitoRawOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dAfnitoRawOutputs",
    "V_3D_AFNITO_RAW_METADATA",
    "v_3d_afnito_raw",
]
