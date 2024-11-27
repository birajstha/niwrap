# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3DDOT_BETA_METADATA = Metadata(
    id="3ccc06408d9c3d573076ee49d8aa6d0e1e01b141.boutiques",
    name="3ddot_beta",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3ddotBetaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3ddot_beta(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output text file containing the correlation-like matrix"""


def v_3ddot_beta(
    input_file: InputPathType,
    prefix: str,
    doeta2: bool = False,
    mask: InputPathType | None = None,
    runner: Runner | None = None,
) -> V3ddotBetaOutputs:
    """
    Beta version of updating 3ddot, currently only performing eta2 tests and
    outputting a full matrix to a text file.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_file: Input file with N bricks.
        prefix: Output prefix for the result file.
        doeta2: Required flag for performing eta2 tests.
        mask: Optional mask file within which to take values.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3ddotBetaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DDOT_BETA_METADATA)
    cargs = []
    cargs.append("3ddot_beta")
    cargs.extend([
        "-input",
        execution.input_file(input_file)
    ])
    cargs.extend([
        "-prefix",
        prefix
    ])
    if doeta2:
        cargs.append("-doeta2")
    if mask is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask)
        ])
    ret = V3ddotBetaOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(prefix + "_eta2.dat"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3ddotBetaOutputs",
    "V_3DDOT_BETA_METADATA",
    "v_3ddot_beta",
]
