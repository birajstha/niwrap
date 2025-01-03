# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_NOTES_METADATA = Metadata(
    id="940bc1c01a30bd95a8de66900c6eff7191dde7e1.boutiques",
    name="3dNotes",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dNotesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_notes(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_3d_notes(
    dataset: InputPathType,
    add_note: str | None = None,
    append_history: str | None = None,
    replace_history: str | None = None,
    delete_note: float | None = None,
    print_notes: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> V3dNotesOutputs:
    """
    A program to add, delete and show notes for AFNI datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dataset: AFNI compatible dataset [required].
        add_note: Add the string 'str' to the list of notes.
        append_history: Append the string 'str' to the dataset's history. This\
            can only appear once on the command line.
        replace_history: Replace any existing history note with 'str'. This\
            option cannot be used with '-h'.
        delete_note: Deletes note number num.
        print_notes: Print to stdout the expanded notes.
        help_: Displays this help screen.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dNotesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_NOTES_METADATA)
    cargs = []
    cargs.append("3dNotes")
    if add_note is not None:
        cargs.extend([
            "-a",
            add_note
        ])
    if append_history is not None:
        cargs.extend([
            "-h",
            append_history
        ])
    if replace_history is not None:
        cargs.extend([
            "-HH",
            replace_history
        ])
    if delete_note is not None:
        cargs.extend([
            "-d",
            str(delete_note)
        ])
    if print_notes:
        cargs.append("-ses")
    if help_:
        cargs.append("-help")
    cargs.append(execution.input_file(dataset))
    ret = V3dNotesOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dNotesOutputs",
    "V_3D_NOTES_METADATA",
    "v_3d_notes",
]
