# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MAKE_DYADIC_VECTORS_METADATA = Metadata(
    id="67f4c0d9c7195c1019d094d8a0a7b14650e07b5c.boutiques",
    name="make_dyadic_vectors",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class MakeDyadicVectorsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `make_dyadic_vectors(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output file containing the generated dyadic vectors"""


def make_dyadic_vectors(
    theta_vol: InputPathType,
    phi_vol: InputPathType,
    output: str,
    mask: InputPathType | None = None,
    perc: float | None = None,
    runner: Runner | None = None,
) -> MakeDyadicVectorsOutputs:
    """
    Generate dyadic vectors from theta and phi volumes.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        theta_vol: Theta volume input file.
        phi_vol: Phi volume input file.
        output: Output file.
        mask: Mask input file (optional).
        perc: Percentage angle of the output cone of uncertainty (output will\
            be in degrees).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MakeDyadicVectorsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MAKE_DYADIC_VECTORS_METADATA)
    cargs = []
    cargs.append("make_dyadic_vectors")
    cargs.append(execution.input_file(theta_vol))
    cargs.append(execution.input_file(phi_vol))
    if mask is not None:
        cargs.append(execution.input_file(mask))
    cargs.append(output)
    if perc is not None:
        cargs.append(str(perc))
    ret = MakeDyadicVectorsOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(output),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MAKE_DYADIC_VECTORS_METADATA",
    "MakeDyadicVectorsOutputs",
    "make_dyadic_vectors",
]
