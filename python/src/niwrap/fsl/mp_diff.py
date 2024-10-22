# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MP_DIFF_METADATA = Metadata(
    id="b9fb35064a1aa1d56c72652cc56c283ce72ac177.boutiques",
    name="mp_diff",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class MpDiffOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mp_diff(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """File containing squared motion parameters, temporal difference of motion
    parameters, and squared differenced values."""


def mp_diff(
    reg_file: InputPathType,
    diff_reg_file: str,
    runner: Runner | None = None,
) -> MpDiffOutputs:
    """
    Generates a file with specific motion parameter calculations useful for
    accounting for 'spin history' effects and other variations not accounted for by
    motion correction.
    
    Author: Unknown
    
    Args:
        reg_file: Input file containing registration parameters (e.g.,\
            regparam.dat).
        diff_reg_file: Output file with differenced registration parameters\
            (e.g., diffregparam.dat).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MpDiffOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MP_DIFF_METADATA)
    cargs = []
    cargs.append("mp_diff")
    cargs.append(execution.input_file(reg_file))
    cargs.append(diff_reg_file)
    ret = MpDiffOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(diff_reg_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MP_DIFF_METADATA",
    "MpDiffOutputs",
    "mp_diff",
]