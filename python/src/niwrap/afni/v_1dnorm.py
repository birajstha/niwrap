# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_1DNORM_METADATA = Metadata(
    id="ea6e83597c9dc8fb3895db8c36d06ddc6f559447.boutiques",
    name="1dnorm",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V1dnormOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1dnorm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    normalized_output: OutputPathType
    """Normalized output AFNI *.1D file"""


def v_1dnorm(
    infile: InputPathType,
    outfile: str,
    norm1: bool = False,
    normx: bool = False,
    demean: bool = False,
    demed: bool = False,
    runner: Runner | None = None,
) -> V1dnormOutputs:
    """
    Normalize columns of a 1D file (AFNI ASCII list of numbers).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        infile: Input AFNI *.1D file (ASCII list of numbers arranged in\
            columns); if '-' input will be read from stdin.
        outfile: Output AFNI *.1D file (normalized); if '-' output will be\
            written to stdout.
        norm1: Normalize so sum of absolute values is 1 (L_1 norm).
        normx: Normalize so that max absolute value is 1 (L_infinity norm).
        demean: Subtract each column's mean before normalizing.
        demed: Subtract each column's median before normalizing.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dnormOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1DNORM_METADATA)
    cargs = []
    cargs.append("1dnorm")
    cargs.append(execution.input_file(infile))
    cargs.append(outfile)
    if norm1:
        cargs.append("-norm1")
    if normx:
        cargs.append("-normx")
    if demean:
        cargs.append("-demean")
    if demed:
        cargs.append("-demed")
    ret = V1dnormOutputs(
        root=execution.output_file("."),
        normalized_output=execution.output_file(outfile),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V1dnormOutputs",
    "V_1DNORM_METADATA",
    "v_1dnorm",
]
