# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_LABEL_CALC_METADATA = Metadata(
    id="4566c0b5206cd4d9fc63822cdb713e50b1ee033e.boutiques",
    name="mris_label_calc",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisLabelCalcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_label_calc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_label: OutputPathType
    """The resulting label file after operation"""


def mris_label_calc(
    command: typing.Literal["union", "intersect", "invert", "erode", "dilate"],
    input1: InputPathType,
    input2: InputPathType,
    output: str,
    runner: Runner | None = None,
) -> MrisLabelCalcOutputs:
    """
    Tool for surface label calculations.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        command: Command to perform on input labels.
        input1: First input label file.
        input2: Second input label file (used for 'invert', 'erode', 'dilate'\
            operations).
        output: Output label file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisLabelCalcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_LABEL_CALC_METADATA)
    cargs = []
    cargs.append("mris_label_calc")
    cargs.append(command)
    cargs.append(execution.input_file(input1))
    cargs.append(execution.input_file(input2))
    cargs.append(output)
    ret = MrisLabelCalcOutputs(
        root=execution.output_file("."),
        output_label=execution.output_file(output + ".label"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_LABEL_CALC_METADATA",
    "MrisLabelCalcOutputs",
    "mris_label_calc",
]
