# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

REGDAT2XFM_METADATA = Metadata(
    id="d24c0503b644852ba5fb4efc153e9c4d555ad111.boutiques",
    name="regdat2xfm",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class Regdat2xfmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `regdat2xfm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def regdat2xfm(
    input_file: InputPathType,
    output_file: str,
    runner: Runner | None = None,
) -> Regdat2xfmOutputs:
    """
    This tool has been removed from the current version of FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: Input file (registration data).
        output_file: Output file (transformation matrix).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Regdat2xfmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(REGDAT2XFM_METADATA)
    cargs = []
    cargs.append("regdat2xfm")
    cargs.append(execution.input_file(input_file))
    cargs.append(output_file)
    ret = Regdat2xfmOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "REGDAT2XFM_METADATA",
    "Regdat2xfmOutputs",
    "regdat2xfm",
]