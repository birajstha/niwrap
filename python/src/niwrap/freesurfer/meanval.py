# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MEANVAL_METADATA = Metadata(
    id="abff5f1715da97f4e48f1b5b12b06bbfdebcd6e0.boutiques",
    name="meanval",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MeanvalOutputs(typing.NamedTuple):
    """
    Output object returned when calling `meanval(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    mean_output_file: OutputPathType
    """File containing the mean value calculated"""


def meanval(
    input_file: InputPathType,
    mask_file: InputPathType,
    output_file: str,
    avgwf_flag: bool = False,
    runner: Runner | None = None,
) -> MeanvalOutputs:
    """
    Tool to calculate the mean value of an image within a mask.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: Input volume file.
        mask_file: Mask file.
        output_file: Output file where mean value will be stored.
        avgwf_flag: Flag to calculate the average waveform.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MeanvalOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MEANVAL_METADATA)
    cargs = []
    cargs.append("meanval")
    cargs.extend([
        "--i",
        execution.input_file(input_file)
    ])
    cargs.extend([
        "--m",
        execution.input_file(mask_file)
    ])
    cargs.extend([
        "--o",
        output_file
    ])
    if avgwf_flag:
        cargs.append("--avgwf")
    ret = MeanvalOutputs(
        root=execution.output_file("."),
        mean_output_file=execution.output_file(output_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MEANVAL_METADATA",
    "MeanvalOutputs",
    "meanval",
]
