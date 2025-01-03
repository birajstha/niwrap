# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TRAC_PREPROC_METADATA = Metadata(
    id="5854dffca5b99ca0a5c033e626a1874da235aa39.boutiques",
    name="trac-preproc",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class TracPreprocOutputs(typing.NamedTuple):
    """
    Output object returned when calling `trac_preproc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def trac_preproc(
    dmrirc_file: InputPathType,
    log_file: str | None = None,
    nolog: bool = False,
    cmd_file: str | None = None,
    nocmd: bool = False,
    no_isrunning: bool = False,
    umask: str | None = None,
    group_id: str | None = None,
    allow_core_dump: bool = False,
    debug: bool = False,
    dontrun: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> TracPreprocOutputs:
    """
    Tractography pre-processing for a single subject.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        dmrirc_file: dmrirc file (see dmrirc.example).
        log_file: Log file; default is trac-all.log in the same dir as dmrirc.
        nolog: Do not save a log file.
        cmd_file: Cmd file; default is trac-all.cmd in the same dir as dmrirc.
        nocmd: Do not save a cmd file.
        no_isrunning: Do not check whether this subject is currently being\
            processed.
        umask: Set unix file permission mask (default 002).
        group_id: Check that current group is alpha groupid.
        allow_core_dump: Set coredump limit to unlimited.
        debug: Generate much more output.
        dontrun: Do everything but execute each command.
        version: Print version of this script and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TracPreprocOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TRAC_PREPROC_METADATA)
    cargs = []
    cargs.append("trac-preproc")
    cargs.extend([
        "-c",
        execution.input_file(dmrirc_file)
    ])
    if log_file is not None:
        cargs.extend([
            "-log",
            log_file
        ])
    if nolog:
        cargs.append("-nolog")
    if cmd_file is not None:
        cargs.extend([
            "-cmd",
            cmd_file
        ])
    if nocmd:
        cargs.append("-nocmd")
    if no_isrunning:
        cargs.append("-no-isrunning")
    if umask is not None:
        cargs.extend([
            "-umask",
            umask
        ])
    if group_id is not None:
        cargs.extend([
            "-grp",
            group_id
        ])
    if allow_core_dump:
        cargs.append("-allowcoredump")
    if debug:
        cargs.append("-debug")
    if dontrun:
        cargs.append("-dontrun")
    if version:
        cargs.append("-version")
    ret = TracPreprocOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TRAC_PREPROC_METADATA",
    "TracPreprocOutputs",
    "trac_preproc",
]
