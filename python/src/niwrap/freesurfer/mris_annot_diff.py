# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_ANNOT_DIFF_METADATA = Metadata(
    id="66fc64b92af2b8d25899007f79214682b156e3d3.boutiques",
    name="mris_annot_diff",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisAnnotDiffOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_annot_diff(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_annot_diff(
    annot1: InputPathType,
    annot2: InputPathType,
    diff_ctab: bool = False,
    verbose: bool = False,
    runner: Runner | None = None,
) -> MrisAnnotDiffOutputs:
    """
    Compare two surface annotation files. The program works with .annot only.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        annot1: Input .annot file 1.
        annot2: Input .annot file 2.
        diff_ctab: Diff colortable included in .annot.
        verbose: Print details of annotation/colortable differences.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisAnnotDiffOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_ANNOT_DIFF_METADATA)
    cargs = []
    cargs.append("mris_annot_diff")
    cargs.append(execution.input_file(annot1))
    cargs.append(execution.input_file(annot2))
    if diff_ctab:
        cargs.append("--diff-ctab")
    if verbose:
        cargs.append("--verbose")
    ret = MrisAnnotDiffOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_ANNOT_DIFF_METADATA",
    "MrisAnnotDiffOutputs",
    "mris_annot_diff",
]