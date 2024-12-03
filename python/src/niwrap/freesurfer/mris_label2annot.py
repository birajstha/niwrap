# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_LABEL2ANNOT_METADATA = Metadata(
    id="67f30d66c4a858ea344c43f9704f2d647b6aa35d.boutiques",
    name="mris_label2annot",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisLabel2annotOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_label2annot(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    annot_file: OutputPathType
    """Generated annotation file"""


def mris_label2annot(
    subject: str,
    hemi: str,
    ctabfile: InputPathType,
    annotname: str,
    index_offset: float | None = None,
    label_files: list[InputPathType] | None = None,
    annot_path: str | None = None,
    labeldir: str | None = None,
    ldir_default: bool = False,
    no_unknown: bool = False,
    thresh: float | None = None,
    maxstatwinner: bool = False,
    surf: str | None = None,
    subjects_dir: str | None = None,
    runner: Runner | None = None,
) -> MrisLabel2annotOutputs:
    """
    Converts a set of surface labels to an annotation file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: FreeSurfer subject.
        hemi: Hemisphere (lh or rh).
        ctabfile: Colortable file (like FreeSurferColorLUT.txt).
        annotname: Output annotation name.
        index_offset: Add to label number to get CTAB index.
        label_files: Label file(s).
        annot_path: Full name/path of annotation file.
        labeldir: Directory with label files when not using --l.
        ldir_default: Use subject/labels as label directory.
        no_unknown: Do not map unhit labels to index 0.
        thresh: Threshold label by stats field.
        maxstatwinner: Keep label with highest 'stat' value.
        surf: Surface name, default is orig.
        subjects_dir: Subjects Directory.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisLabel2annotOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_LABEL2ANNOT_METADATA)
    cargs = []
    cargs.append("mris_label2annot")
    cargs.extend([
        "-s",
        subject
    ])
    cargs.extend([
        "-h",
        hemi
    ])
    cargs.extend([
        "-ctab",
        execution.input_file(ctabfile)
    ])
    cargs.extend([
        "-a",
        annotname
    ])
    if index_offset is not None:
        cargs.extend([
            "--offset",
            str(index_offset)
        ])
    if label_files is not None:
        cargs.extend([
            "--l",
            *[execution.input_file(f) for f in label_files]
        ])
    if annot_path is not None:
        cargs.extend([
            "--annot-path",
            annot_path
        ])
    if labeldir is not None:
        cargs.extend([
            "--ldir",
            labeldir
        ])
    if ldir_default:
        cargs.append("--ldir-default")
    if no_unknown:
        cargs.append("--no-unknown")
    if thresh is not None:
        cargs.extend([
            "--thresh",
            str(thresh)
        ])
    if maxstatwinner:
        cargs.append("--maxstatwinner")
    if surf is not None:
        cargs.extend([
            "--surf",
            surf
        ])
    if subjects_dir is not None:
        cargs.extend([
            "--sd",
            subjects_dir
        ])
    ret = MrisLabel2annotOutputs(
        root=execution.output_file("."),
        annot_file=execution.output_file(hemi + "." + annotname + ".annot"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_LABEL2ANNOT_METADATA",
    "MrisLabel2annotOutputs",
    "mris_label2annot",
]