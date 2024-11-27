# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__THICKNESS_MASTER_METADATA = Metadata(
    id="7cbe201588fb28fa02cdf63392c9f32c09dd8fea.boutiques",
    name="@thickness_master",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VThicknessMasterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__thickness_master(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_bb_dir: OutputPathType | None
    """Output directory for ball and box method"""
    output_erode_dir: OutputPathType | None
    """Output directory for erosion method"""
    output_in2out_dir: OutputPathType | None
    """Output directory for in2out method"""


def v__thickness_master(
    maskset: InputPathType,
    surfset: InputPathType,
    outdir: str | None = None,
    runner: Runner | None = None,
) -> VThicknessMasterOutputs:
    """
    Compute cortical thickness using mask and surface datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        maskset: Mask dataset to find thickness.
        surfset: Surface dataset to use for normals into the volume.
        outdir: Output directory base name. The output will be placed in a\
            directory with thick_base in its name (e.g., mmmm_bb, mmmm_erode,\
            mmmm_in2out).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VThicknessMasterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__THICKNESS_MASTER_METADATA)
    cargs = []
    cargs.append("@thickness_master")
    cargs.extend([
        "-maskset",
        execution.input_file(maskset)
    ])
    cargs.extend([
        "-surfset",
        execution.input_file(surfset)
    ])
    if outdir is not None:
        cargs.extend([
            "-outdir",
            outdir
        ])
    ret = VThicknessMasterOutputs(
        root=execution.output_file("."),
        output_bb_dir=execution.output_file(outdir + "_bb/") if (outdir is not None) else None,
        output_erode_dir=execution.output_file(outdir + "_erode/") if (outdir is not None) else None,
        output_in2out_dir=execution.output_file(outdir + "_in2out/") if (outdir is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VThicknessMasterOutputs",
    "V__THICKNESS_MASTER_METADATA",
    "v__thickness_master",
]
