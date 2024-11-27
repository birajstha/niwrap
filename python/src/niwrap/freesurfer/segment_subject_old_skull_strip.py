# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SEGMENT_SUBJECT_OLD_SKULL_STRIP_METADATA = Metadata(
    id="abc48359fac304f034867897b978186bcd82c5e7.boutiques",
    name="segment_subject_old_skull_strip",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class SegmentSubjectOldSkullStripOutputs(typing.NamedTuple):
    """
    Output object returned when calling `segment_subject_old_skull_strip(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_xfm_file: OutputPathType
    """Resulting output xfm file"""
    log_output_file: OutputPathType | None
    """Generated log file"""


def segment_subject_old_skull_strip(
    input_volume: InputPathType,
    output_xfm: str,
    log_file: str | None = None,
    help_flag: bool = False,
    debug_flag: bool = False,
    version_flag: bool = False,
    runner: Runner | None = None,
) -> SegmentSubjectOldSkullStripOutputs:
    """
    Front-end for MINCs mritotal for computing the talairach transform that maps the
    input volume to the MNI305.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input volume file.
        output_xfm: Output xfm file.
        log_file: Log file. Default is outdir/talarach.log.
        help_flag: Print help and exit.
        debug_flag: Turn on debugging.
        version_flag: Print version and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SegmentSubjectOldSkullStripOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SEGMENT_SUBJECT_OLD_SKULL_STRIP_METADATA)
    cargs = []
    cargs.append("mri_nu_correct.mni")
    cargs.extend([
        "-i",
        "-" + execution.input_file(input_volume)
    ])
    cargs.extend([
        "-xfm",
        "-" + output_xfm
    ])
    if log_file is not None:
        cargs.extend([
            "--log",
            log_file
        ])
    if help_flag:
        cargs.append("--help")
    if debug_flag:
        cargs.append("--debug")
    if version_flag:
        cargs.append("--version")
    ret = SegmentSubjectOldSkullStripOutputs(
        root=execution.output_file("."),
        output_xfm_file=execution.output_file(output_xfm),
        log_output_file=execution.output_file(log_file) if (log_file is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SEGMENT_SUBJECT_OLD_SKULL_STRIP_METADATA",
    "SegmentSubjectOldSkullStripOutputs",
    "segment_subject_old_skull_strip",
]
