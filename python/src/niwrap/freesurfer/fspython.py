# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSPYTHON_METADATA = Metadata(
    id="dfe661e4b95df49bda1a5aa1bf490874896a0fea.boutiques",
    name="fspython",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class FspythonOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fspython(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fspython(
    args: list[str] | None = None,
    runner: Runner | None = None,
) -> FspythonOutputs:
    """
    Freesurfer's embedded Python interpreter.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        args: Arguments passed to the program.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FspythonOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSPYTHON_METADATA)
    cargs = []
    cargs.append("/usr/local/freesurfer/python/bin/python3")
    cargs.append("[OPTION]")
    if args is not None:
        cargs.extend(args)
    ret = FspythonOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSPYTHON_METADATA",
    "FspythonOutputs",
    "fspython",
]