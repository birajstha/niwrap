# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

POSSUM_SUM_METADATA = Metadata(
    id="46cdd0b1f4a3ba6ef291b09c6aeec5a8c6c5d7d9.boutiques",
    name="possum_sum",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class PossumSumOutputs(typing.NamedTuple):
    """
    Output object returned when calling `possum_sum(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Sum of all input signals from processors"""


def possum_sum(
    input_signal: InputPathType,
    output_signal: InputPathType,
    num_processors: int | None = None,
    verbose_flag: bool = False,
    runner: Runner | None = None,
) -> PossumSumOutputs:
    """
    Sum of output signals from multiple possum processors.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_signal: Input signal for one processor (possum output matrix).
        output_signal: Output signal: sum of all the processors (possum matrix\
            form).
        num_processors: Number of processors.
        verbose_flag: Switch on diagnostic messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PossumSumOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(POSSUM_SUM_METADATA)
    cargs = []
    cargs.append("possum_sum")
    cargs.extend([
        "-i",
        execution.input_file(input_signal)
    ])
    cargs.extend([
        "-o",
        execution.input_file(output_signal)
    ])
    if num_processors is not None:
        cargs.extend([
            "-n",
            str(num_processors)
        ])
    if verbose_flag:
        cargs.append("-v")
    ret = PossumSumOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(pathlib.Path(output_signal).name),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "POSSUM_SUM_METADATA",
    "PossumSumOutputs",
    "possum_sum",
]
