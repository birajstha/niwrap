# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

PTOZ_METADATA = Metadata(
    id="e4fc1ae7a2db14a20f16ef71c261bb1f39199c0b",
    name="ptoz",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="spm/spm12:latest",
)


class PtozOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ptoz(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def ptoz(
    p_value: float | int,
    tail_flag: bool = False,
    grf_flag: float | int | None = None,
    runner: Runner = None,
) -> PtozOutputs:
    """
    ptoz by Statistical Parametric Mapping (SPM).
    
    Convert p-values to z-values.
    
    Args:
        p_value: p-value to convert.
        tail_flag: Use 2-tailed conversion.
        grf_flag: Use GRF maximum-height theory instead of Gaussian pdf.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PtozOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PTOZ_METADATA)
    cargs = []
    cargs.append("ptoz")
    cargs.append(str(p_value))
    if tail_flag:
        cargs.append("-2")
    if grf_flag is not None:
        cargs.extend(["-g", str(grf_flag)])
    ret = PtozOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "PTOZ_METADATA",
    "PtozOutputs",
    "ptoz",
]
