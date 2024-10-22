# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

COMPUTE_INTERRATER_VARIABILITY_CSH_METADATA = Metadata(
    id="7de8fa40a7749dafc1239646d03c80801e6cc231.boutiques",
    name="compute_interrater_variability.csh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class ComputeInterraterVariabilityCshOutputs(typing.NamedTuple):
    """
    Output object returned when calling `compute_interrater_variability_csh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file_1: OutputPathType
    """Output file containing mean Hausdorff distance."""
    output_file_2: OutputPathType
    """Output file containing max Hausdorff distance."""
    output_file_3: OutputPathType
    """Output file containing label volume difference, Dice, and Jaccard overlap
    measures."""


def compute_interrater_variability_csh(
    label_vol1: InputPathType,
    label_vol2: InputPathType,
    output_prefix: str,
    runner: Runner | None = None,
) -> ComputeInterraterVariabilityCshOutputs:
    """
    Computes the interrater variability between label volumes from different raters
    or time points using several metrics.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        label_vol1: Label volume from rater 1.
        label_vol2: Label volume from rater 2.
        output_prefix: Prefix for the output text files containing results. A\
            total of three files will be produced.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ComputeInterraterVariabilityCshOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(COMPUTE_INTERRATER_VARIABILITY_CSH_METADATA)
    cargs = []
    cargs.append("compute_interrater_variability")
    cargs.append("--vol1")
    cargs.extend([
        "--vol1",
        execution.input_file(label_vol1)
    ])
    cargs.append("--vol2")
    cargs.extend([
        "--vol2",
        execution.input_file(label_vol2)
    ])
    cargs.append("--out")
    cargs.extend([
        "--out",
        output_prefix
    ])
    ret = ComputeInterraterVariabilityCshOutputs(
        root=execution.output_file("."),
        output_file_1=execution.output_file(output_prefix + "_file1.txt"),
        output_file_2=execution.output_file(output_prefix + "_file2.txt"),
        output_file_3=execution.output_file(output_prefix + "_file3.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "COMPUTE_INTERRATER_VARIABILITY_CSH_METADATA",
    "ComputeInterraterVariabilityCshOutputs",
    "compute_interrater_variability_csh",
]