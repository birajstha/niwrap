# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_DIFF_METADATA = Metadata(
    id="30172af00f20644762a6e2ce032311fb482cfc14.boutiques",
    name="mris_diff",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisDiffOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_diff(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_diff(
    surface1: InputPathType,
    surface2: InputPathType,
    subject1: str,
    subject2: str,
    hemisphere: str,
    subj_dir1: str | None = None,
    subj_dir2: str | None = None,
    runner: Runner | None = None,
) -> MrisDiffOutputs:
    """
    A tool for comparing differences between surface files in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        surface1: First surface file.
        surface2: Second surface file.
        subject1: Subject 1 name.
        subject2: Subject 2 name.
        hemisphere: Hemisphere (rh or lh).
        subj_dir1: Directory for Subject 1 (default is SUBJECTS_DIR).
        subj_dir2: Directory for Subject 2 (default is SUBJECTS_DIR).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisDiffOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_DIFF_METADATA)
    cargs = []
    cargs.append("mris_diff")
    cargs.append(execution.input_file(surface1))
    cargs.append(execution.input_file(surface2))
    cargs.extend([
        "--s1",
        subject1
    ])
    cargs.extend([
        "--s2",
        subject2
    ])
    if subj_dir1 is not None:
        cargs.extend([
            "--sd1",
            subj_dir1
        ])
    if subj_dir2 is not None:
        cargs.extend([
            "--sd2",
            subj_dir2
        ])
    cargs.extend([
        "--hemi",
        hemisphere
    ])
    ret = MrisDiffOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_DIFF_METADATA",
    "MrisDiffOutputs",
    "mris_diff",
]
