# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MORPH_ONLY_SUBJECT_RH_METADATA = Metadata(
    id="f5e066989871c67bda328c2a6375ebf27199e0ac.boutiques",
    name="morph_only_subject-rh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MorphOnlySubjectRhOutputs(typing.NamedTuple):
    """
    Output object returned when calling `morph_only_subject_rh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_files: OutputPathType
    """The output morphing files for the right hemisphere generated by the
    process."""


def morph_only_subject_rh(
    subject_dir: InputPathType,
    runner: Runner | None = None,
) -> MorphOnlySubjectRhOutputs:
    """
    This tool processes morph-specific operations for the right hemisphere of the
    brain using Freesurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_dir: Path to the subject's directory containing the necessary\
            input files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MorphOnlySubjectRhOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MORPH_ONLY_SUBJECT_RH_METADATA)
    cargs = []
    cargs.extend([
        "-rh",
        "morph_only_subject" + execution.input_file(subject_dir)
    ])
    ret = MorphOnlySubjectRhOutputs(
        root=execution.output_file("."),
        output_files=execution.output_file("/usr/local/freesurfer/subjects/[OPTIONS]/rh.morph"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MORPH_ONLY_SUBJECT_RH_METADATA",
    "MorphOnlySubjectRhOutputs",
    "morph_only_subject_rh",
]
