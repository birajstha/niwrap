# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FVCOMPARE_METADATA = Metadata(
    id="84e27ef54cc73075db70cca3ebbdd40631c9472d.boutiques",
    name="fvcompare",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class FvcompareOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fvcompare(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fvcompare(
    subject1: str,
    subject2: str,
    subject_dir1: str | None = None,
    subject_dir2: str | None = None,
    name1: str | None = None,
    name2: str | None = None,
    color1: str | None = None,
    volume: str | None = None,
    segmentation: str | None = None,
    aseg: bool = False,
    no_seg: bool = False,
    right_hemi: bool = False,
    no_surf: bool = False,
    gray_levels: list[float] | None = None,
    cursor_position: list[float] | None = None,
    zoom_level: float | None = None,
    annotation: str | None = None,
    aparc: bool = False,
    inflated: bool = False,
    white: bool = False,
    orig: bool = False,
    surf_name: str | None = None,
    pointset: InputPathType | None = None,
    wot2: bool = False,
    runner: Runner | None = None,
) -> FvcompareOutputs:
    """
    Simultaneously loads volume, segmentation, and surface data from two subjects in
    freeview, for comparing across time or different analysis methods.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject1: Subject 1 identifier.
        subject2: Subject 2 identifier.
        subject_dir1: Directory path for Subject 1.
        subject_dir2: Directory path for Subject 2.
        name1: Name associated with Subject 1 (default: s1).
        name2: Name associated with Subject 2 (default: s2).
        color1: Set surface colors for Subject 1.
        volume: Volume name found in subject/mri (default: brainmask.mgz, can\
            have multiple).
        segmentation: Segmentation name found in subject/mri (default:\
            aparc+aseg.mgz, can have multiple).
        aseg: Add aseg.mgz to segmentation list.
        no_seg: Do not display segmentations.
        right_hemi: Only display right hemisphere.
        no_surf: Do not display surfaces.
        gray_levels: Set gray scale levels.
        cursor_position: Place cursor at given location and center Field of\
            View.
        zoom_level: Set zoom level.
        annotation: Load annotation onto surfaces.
        aparc: Load aparc.annot onto surfaces.
        inflated: Load inflated surfaces in addition to white and pial.
        white: Only show white surfaces.
        orig: Only show orig.nofix and orig surfaces.
        surf_name: Only show specified surface name.
        pointset: Load point set file.
        wot2: Include the ?h.woT2.pial surfs.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FvcompareOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FVCOMPARE_METADATA)
    cargs = []
    cargs.append("fvcompare")
    cargs.extend([
        "--s1",
        subject1
    ])
    cargs.extend([
        "--s2",
        subject2
    ])
    if subject_dir1 is not None:
        cargs.extend([
            "--sd1",
            subject_dir1
        ])
    if subject_dir2 is not None:
        cargs.extend([
            "--sd2",
            subject_dir2
        ])
    if name1 is not None:
        cargs.extend([
            "--n1",
            name1
        ])
    if name2 is not None:
        cargs.extend([
            "--n2",
            name2
        ])
    if color1 is not None:
        cargs.extend([
            "--c1",
            color1
        ])
    if volume is not None:
        cargs.extend([
            "--vol",
            volume
        ])
    if segmentation is not None:
        cargs.extend([
            "--seg",
            segmentation
        ])
    if aseg:
        cargs.append("--aseg")
    if no_seg:
        cargs.append("--no-seg")
    if right_hemi:
        cargs.append("--rh")
    if no_surf:
        cargs.append("--no-surf")
    if gray_levels is not None:
        cargs.extend([
            "--gray",
            *map(str, gray_levels)
        ])
    if cursor_position is not None:
        cargs.extend([
            "--crs",
            *map(str, cursor_position)
        ])
    if zoom_level is not None:
        cargs.extend([
            "--zoom",
            str(zoom_level)
        ])
    if annotation is not None:
        cargs.extend([
            "--annot",
            annotation
        ])
    if aparc:
        cargs.append("--aparc")
    if inflated:
        cargs.append("--inflated")
    if white:
        cargs.append("--white")
    if orig:
        cargs.append("--orig")
    if surf_name is not None:
        cargs.extend([
            "--surf",
            surf_name
        ])
    if pointset is not None:
        cargs.extend([
            "--p",
            execution.input_file(pointset)
        ])
    if wot2:
        cargs.append("--wot2")
    ret = FvcompareOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FVCOMPARE_METADATA",
    "FvcompareOutputs",
    "fvcompare",
]