# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FSLADD_METADATA = Metadata(
    id="cdbbff5ffc760d176ade851d8308f9d5b84fa222",
    name="fsladd",
)


class FsladdOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsladd(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    resulting_output: OutputPathType
    """Resulting output file"""


def fsladd(
    output_file: InputPathType,
    volume_list: list[InputPathType],
    mean_flag: bool = False,
    scale_flag: bool = False,
    runner: Runner = None,
) -> FsladdOutputs:
    """
    fsladd by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    Tool for adding or averaging multiple input volumes.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Fslutils
    
    Args:
        output_file: Output volume file.
        volume_list: List of input volumes.
        mean_flag: Calculate mean instead of sum.
        scale_flag: Scale each input image mean to 1000 before processing.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FsladdOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLADD_METADATA)
    cargs = []
    cargs.append("fsladd")
    cargs.append(execution.input_file(output_file))
    if mean_flag:
        cargs.append("-m")
    if scale_flag:
        cargs.append("-s")
    cargs.extend([execution.input_file(f) for f in volume_list])
    ret = FsladdOutputs(
        root=execution.output_file("."),
        resulting_output=execution.output_file(f"{pathlib.Path(output_file).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLADD_METADATA",
    "FsladdOutputs",
    "fsladd",
]
