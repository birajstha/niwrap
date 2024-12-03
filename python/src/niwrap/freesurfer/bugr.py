# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

BUGR_METADATA = Metadata(
    id="61b1c8588fe75d759f05f238db179fab105dd284.boutiques",
    name="bugr",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class BugrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `bugr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def bugr(
    subject_name: str,
    command_line: str,
    error_message: str,
    log_file: InputPathType | None = None,
    runner: Runner | None = None,
) -> BugrOutputs:
    """
    Utility for generating and reporting FreeSurfer bugs.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_name: Subject name to include in the bug report.
        command_line: The entire command-line executed.
        error_message: The error message generated.
        log_file: Log file path of the subject's recon-all process.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BugrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BUGR_METADATA)
    cargs = []
    cargs.append("bugr")
    cargs.extend([
        "-subject",
        subject_name
    ])
    cargs.extend([
        "-command",
        command_line
    ])
    cargs.extend([
        "-error",
        error_message
    ])
    if log_file is not None:
        cargs.extend([
            "-log",
            execution.input_file(log_file)
        ])
    ret = BugrOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "BUGR_METADATA",
    "BugrOutputs",
    "bugr",
]