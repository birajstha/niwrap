# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_FRIEDMAN_METADATA = Metadata(
    id="39739dbe60149a8c929fe468d57b937cc221945c.boutiques",
    name="3dFriedman",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dFriedmanOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_friedman(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Friedman statistics output file"""


def v_3d_friedman(
    levels: int,
    datasets: list[InputPathType],
    output_prefix: str,
    workmem: int | None = None,
    voxel_num: int | None = None,
    runner: Runner | None = None,
) -> V3dFriedmanOutputs:
    """
    Performs nonparametric Friedman test for randomized complete block design
    experiments.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        levels: Number of treatments.
        datasets: Data sets for each treatment.
        output_prefix: Prefix for the output files.
        workmem: Number of megabytes of RAM to use for statistical workspace.
        voxel_num: Screen output for a specific voxel number.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dFriedmanOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_FRIEDMAN_METADATA)
    cargs = []
    cargs.append("3dFriedman")
    cargs.append(str(levels))
    cargs.extend([
        "-dset",
        *[execution.input_file(f) for f in datasets]
    ])
    if workmem is not None:
        cargs.extend([
            "-workmem",
            str(workmem)
        ])
    if voxel_num is not None:
        cargs.extend([
            "-voxel",
            str(voxel_num)
        ])
    cargs.extend([
        "-out",
        output_prefix
    ])
    ret = V3dFriedmanOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(output_prefix + "*"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dFriedmanOutputs",
    "V_3D_FRIEDMAN_METADATA",
    "v_3d_friedman",
]
