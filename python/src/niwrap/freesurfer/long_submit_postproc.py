# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

LONG_SUBMIT_POSTPROC_METADATA = Metadata(
    id="f5d6d8fc46443ea959ac2b4347964b2a0edf8163.boutiques",
    name="long_submit_postproc",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class LongSubmitPostprocOutputs(typing.NamedTuple):
    """
    Output object returned when calling `long_submit_postproc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def long_submit_postproc(
    qdec: InputPathType,
    prog: str,
    flags: str | None = None,
    dir_: str | None = None,
    simulate: bool = False,
    pause: float | None = 13,
    max_: float | None = 100,
    queue_: str | None = None,
    runner: Runner | None = None,
) -> LongSubmitPostprocOutputs:
    """
    Submits jobs to the cluster (either seychelles or launchpad at NMR) for
    longitudinal post-processing.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        qdec: QDEC table file specifying the subjects and time points.
        prog: Longitudinal script to call.
        flags: Parameters (without --qdec) to pass to prog (using quotes ...).
        dir_: Directory to store sub-tables and command files.
        simulate: Do not submit anything, just print commands.
        pause: Pause in seconds between submissions.
        max_: Maximum number of jobs for this user.
        queue_: Special queue to submit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `LongSubmitPostprocOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LONG_SUBMIT_POSTPROC_METADATA)
    cargs = []
    cargs.append("long_submit_postproc")
    cargs.extend([
        "--qdec",
        execution.input_file(qdec)
    ])
    cargs.extend([
        "--prog",
        prog
    ])
    if flags is not None:
        cargs.extend([
            "--flags",
            flags
        ])
    if dir_ is not None:
        cargs.extend([
            "--dir",
            dir_
        ])
    if simulate:
        cargs.append("--simulate")
    if pause is not None:
        cargs.extend([
            "--pause",
            str(pause)
        ])
    if max_ is not None:
        cargs.extend([
            "--max",
            str(max_)
        ])
    if queue_ is not None:
        cargs.extend([
            "--queue",
            queue_
        ])
    ret = LongSubmitPostprocOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "LONG_SUBMIT_POSTPROC_METADATA",
    "LongSubmitPostprocOutputs",
    "long_submit_postproc",
]
