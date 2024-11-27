# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MAKE_SEGVOL_TABLE_METADATA = Metadata(
    id="584e18cf5964aa90ad96025eab578f07dcec865b.boutiques",
    name="make-segvol-table",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MakeSegvolTableOutputs(typing.NamedTuple):
    """
    Output object returned when calling `make_segvol_table(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_table: OutputPathType
    """Output text file containing the table of subcortical structure
    volumes."""


def make_segvol_table(
    subjects: list[str],
    subject_file: InputPathType,
    outfile: str,
    idmap: InputPathType | None = None,
    structure_ids: list[str] | None = None,
    segdir: str | None = None,
    subjects_dir: str | None = None,
    umask: str | None = None,
    version: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> MakeSegvolTableOutputs:
    """
    Creates a table of volumes of subcortical structures for a given list of
    subjects using FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjects: List of subject IDs. Each subject should be specified with a\
            separate -s flag.
        subject_file: Path to a file containing a list of subjects.
        outfile: Output file where the table will be saved.
        idmap: File with structure name and id number. Default is\
            FREESURFER_HOME/tkmeditColorsCMA.
        structure_ids: Names of structures to include in the table. Defaults to\
            all structures.
        segdir: Segmentation subdirectory name. Default is 'aseg'.
        subjects_dir: Path to the subjects directory. Default is SUBJECTS_DIR\
            environment variable.
        umask: Set UNIX file permission mask.
        version: Print version and exit.
        help_: Display help information.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MakeSegvolTableOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MAKE_SEGVOL_TABLE_METADATA)
    cargs = []
    cargs.append("make-segvol-table")
    cargs.extend([
        "-s",
        *subjects
    ])
    cargs.extend([
        "-sf",
        execution.input_file(subject_file)
    ])
    cargs.extend([
        "-o",
        outfile
    ])
    if idmap is not None:
        cargs.extend([
            "-idmap",
            execution.input_file(idmap)
        ])
    if structure_ids is not None:
        cargs.extend([
            "-id",
            *structure_ids
        ])
    if segdir is not None:
        cargs.extend([
            "-segdir",
            segdir
        ])
    if subjects_dir is not None:
        cargs.extend([
            "-sd",
            subjects_dir
        ])
    if umask is not None:
        cargs.extend([
            "-umask",
            umask
        ])
    if version:
        cargs.append("-version")
    if help_:
        cargs.append("-help")
    ret = MakeSegvolTableOutputs(
        root=execution.output_file("."),
        output_table=execution.output_file(outfile),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MAKE_SEGVOL_TABLE_METADATA",
    "MakeSegvolTableOutputs",
    "make_segvol_table",
]
