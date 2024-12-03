# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

XCORR_METADATA = Metadata(
    id="9e4522b49e6cabe069fc758dd70b99c8feb9830e.boutiques",
    name="xcorr",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class XcorrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `xcorr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_xcorrfile: OutputPathType
    """Output xcorr file"""
    log_output: OutputPathType | None
    """Log of xcorr execution"""


def xcorr(
    input1: InputPathType,
    input2: InputPathType,
    output: str,
    log_file: str | None = None,
    tmp_dir: str | None = None,
    no_cleanup: bool = False,
    runner: Runner | None = None,
) -> XcorrOutputs:
    """
    Computes the voxel-for-voxel correlation coefficient between two volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input1: First input volume file.
        input2: Second input volume file.
        output: Output xcorr file.
        log_file: Log file.
        tmp_dir: Temporary directory.
        no_cleanup: Prevent cleanup of temporary files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `XcorrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(XCORR_METADATA)
    cargs = []
    cargs.append("xcorr")
    cargs.extend([
        "--i1",
        execution.input_file(input1)
    ])
    cargs.extend([
        "--i2",
        execution.input_file(input2)
    ])
    cargs.extend([
        "--o",
        output
    ])
    if log_file is not None:
        cargs.extend([
            "--log",
            log_file
        ])
    if tmp_dir is not None:
        cargs.extend([
            "--tmp",
            tmp_dir
        ])
    if no_cleanup:
        cargs.append("--no-cleanup")
    ret = XcorrOutputs(
        root=execution.output_file("."),
        out_xcorrfile=execution.output_file(output),
        log_output=execution.output_file(log_file) if (log_file is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "XCORR_METADATA",
    "XcorrOutputs",
    "xcorr",
]