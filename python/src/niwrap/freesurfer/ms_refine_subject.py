# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MS_REFINE_SUBJECT_METADATA = Metadata(
    id="c522667edafe63ffe7ee067f5ceb07e59d920d4c.boutiques",
    name="ms_refine_subject",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MsRefineSubjectOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ms_refine_subject(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def ms_refine_subject(
    subjects_dir: str,
    runner: Runner | None = None,
) -> MsRefineSubjectOutputs:
    """
    Unknown.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjects_dir: Directory containing the subject data (e.g.\
            /usr/local/freesurfer/subjects).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MsRefineSubjectOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MS_REFINE_SUBJECT_METADATA)
    cargs = []
    cargs.append("ms_refine_subject")
    cargs.append(subjects_dir)
    ret = MsRefineSubjectOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MS_REFINE_SUBJECT_METADATA",
    "MsRefineSubjectOutputs",
    "ms_refine_subject",
]