# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DEFACE_SUBJECT_METADATA = Metadata(
    id="274e5ad239a83bd50707ef1a9dcf8ce7c5e84775.boutiques",
    name="deface_subject",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class DefaceSubjectOutputs(typing.NamedTuple):
    """
    Output object returned when calling `deface_subject(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume: OutputPathType
    """Defaced output volume."""


def deface_subject(
    subjects_dir: str,
    subject_id: str,
    volume_input: InputPathType,
    volume_output: str,
    runner: Runner | None = None,
) -> DefaceSubjectOutputs:
    """
    Tool for defacing MRI images to anonymize patient data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjects_dir: Directory containing FreeSurfer subject directories.
        subject_id: Subject ID that specifies the subject directory.
        volume_input: Input volume to be defaced.
        volume_output: Output volume after defacing.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DefaceSubjectOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DEFACE_SUBJECT_METADATA)
    cargs = []
    cargs.append("deface_subject")
    cargs.extend([
        "-sdir",
        subjects_dir
    ])
    cargs.extend([
        "-id",
        subject_id
    ])
    cargs.extend([
        "-i",
        execution.input_file(volume_input)
    ])
    cargs.extend([
        "-o",
        volume_output
    ])
    ret = DefaceSubjectOutputs(
        root=execution.output_file("."),
        output_volume=execution.output_file(volume_output),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DEFACE_SUBJECT_METADATA",
    "DefaceSubjectOutputs",
    "deface_subject",
]