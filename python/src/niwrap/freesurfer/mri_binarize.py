# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_BINARIZE_METADATA = Metadata(
    id="97e37d2eb690a5a8992a2d101f133c67b3abb7c2.boutiques",
    name="mri_binarize",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriBinarizeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_binarize(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_volume: OutputPathType
    """The resulting binarized volume."""


def mri_binarize(
    input_volume: InputPathType,
    output_volume: str,
    min_threshold: float | None = None,
    max_threshold: float | None = None,
    pct_threshold: float | None = None,
    rmin: float | None = None,
    rmax: float | None = None,
    fdr_threshold: float | None = None,
    match_values: list[float] | None = None,
    replace_values: list[float] | None = None,
    binval: float | None = None,
    binval_not: float | None = None,
    frame: float | None = None,
    merge_volume: InputPathType | None = None,
    mask_volume: InputPathType | None = None,
    mask_threshold: float | None = None,
    surf_name: str | None = None,
    surf_smooth: float | None = None,
    threads: float | None = None,
    ctx_wm_flag: bool = False,
    all_wm_flag: bool = False,
    ventricles_flag: bool = False,
    wm_vcsf_flag: bool = False,
    gm_flag: bool = False,
    subcort_gm_flag: bool = False,
    scm_lh_flag: bool = False,
    scm_rh_flag: bool = False,
    zero_edges_flag: bool = False,
    zero_slice_edges_flag: bool = False,
    dilate_vertex: str | None = None,
    remove_islands_flag: bool = False,
    fill_holes_flag: bool = False,
    noverbose_flag: bool = False,
    debug_flag: bool = False,
    runner: Runner | None = None,
) -> MriBinarizeOutputs:
    """
    A program to binarize a volume or volume-encoded surface file, with options to
    merge and manipulate binarized output.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input volume to be binarized.
        output_volume: Path to output volume.
        min_threshold: Minimum threshold (default is -inf).
        max_threshold: Maximum threshold (default is +inf).
        pct_threshold: Set threshold to capture top P% of voxels.
        rmin: Compute min threshold based on rmin times global mean.
        rmax: Compute max threshold based on rmax times global mean.
        fdr_threshold: Compute min threshold based on FDR.
        match_values: Binarize based on matching values.
        replace_values: Replace voxels with specified values. Format: V1 V2.
        binval: Set voxel value within threshold to specified value (default is\
            1).
        binval_not: Set voxel value outside threshold range to specified value\
            (default is 0).
        frame: Use specific frame of the input. 0-based index.
        merge_volume: Merge with another volume. Must be the same dimensions as\
            input volume.
        mask_volume: Mask input with a specified mask volume.
        mask_threshold: Set threshold for mask volume (default is 0.5).
        surf_name: Create a surface mesh from the binarization.
        surf_smooth: Smooth the surface mesh iteratively, specifying the number\
            of iterations.
        threads: Specify number of threads to use.
        ctx_wm_flag: Set match values for cerebral white matter.
        all_wm_flag: Set match values for all white matter.
        ventricles_flag: Set match values for ventricles and choroid.
        wm_vcsf_flag: Match for WM and ventricular CSF.
        gm_flag: Match for all WM, VCSF and background, then invert.
        subcort_gm_flag: Match for subcortical gray matter.
        scm_lh_flag: Subcortical mass for left hemisphere.
        scm_rh_flag: Subcortical mass for right hemisphere.
        zero_edges_flag: Set edge voxels to zero.
        zero_slice_edges_flag: Set edge slice voxels to zero.
        dilate_vertex: Dilate vertex to a specific target area.
        remove_islands_flag: Remove islands in the mask.
        fill_holes_flag: Remove holes in the mask.
        noverbose_flag: Suppress verbose output.
        debug_flag: Enable debugging output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriBinarizeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_BINARIZE_METADATA)
    cargs = []
    cargs.append("/usr/local/freesurfer/bin/mri_binarize")
    cargs.extend([
        "--i",
        execution.input_file(input_volume)
    ])
    cargs.extend([
        "--o",
        output_volume
    ])
    if min_threshold is not None:
        cargs.extend([
            "--min",
            str(min_threshold)
        ])
    if max_threshold is not None:
        cargs.extend([
            "--max",
            str(max_threshold)
        ])
    if pct_threshold is not None:
        cargs.extend([
            "--pct",
            str(pct_threshold)
        ])
    if rmin is not None:
        cargs.extend([
            "--rmin",
            str(rmin)
        ])
    if rmax is not None:
        cargs.extend([
            "--rmax",
            str(rmax)
        ])
    if fdr_threshold is not None:
        cargs.extend([
            "--fdr",
            str(fdr_threshold)
        ])
    if match_values is not None:
        cargs.extend([
            "--match",
            *map(str, match_values)
        ])
    if replace_values is not None:
        cargs.extend([
            "--replace",
            *map(str, replace_values)
        ])
    if binval is not None:
        cargs.extend([
            "--binval",
            str(binval)
        ])
    if binval_not is not None:
        cargs.extend([
            "--binvalnot",
            str(binval_not)
        ])
    if frame is not None:
        cargs.extend([
            "--frame",
            str(frame)
        ])
    if merge_volume is not None:
        cargs.extend([
            "--merge",
            execution.input_file(merge_volume)
        ])
    if mask_volume is not None:
        cargs.extend([
            "--mask",
            execution.input_file(mask_volume)
        ])
    if mask_threshold is not None:
        cargs.extend([
            "--mask-thresh",
            str(mask_threshold)
        ])
    if surf_name is not None:
        cargs.extend([
            "--surf",
            surf_name
        ])
    if surf_smooth is not None:
        cargs.extend([
            "--surf-smooth",
            str(surf_smooth)
        ])
    if threads is not None:
        cargs.extend([
            "--threads",
            str(threads)
        ])
    if ctx_wm_flag:
        cargs.append("--ctx-wm")
    if all_wm_flag:
        cargs.append("--all-wm")
    if ventricles_flag:
        cargs.append("--ventricles")
    if wm_vcsf_flag:
        cargs.append("--wm+vcsf")
    if gm_flag:
        cargs.append("--gm")
    if subcort_gm_flag:
        cargs.append("--subcort-gm")
    if scm_lh_flag:
        cargs.append("--scm-lh")
    if scm_rh_flag:
        cargs.append("--scm-rh")
    if zero_edges_flag:
        cargs.append("--zero-edges")
    if zero_slice_edges_flag:
        cargs.append("--zero-slice-edges")
    if dilate_vertex is not None:
        cargs.extend([
            "--dilate-vertex",
            dilate_vertex
        ])
    if remove_islands_flag:
        cargs.append("--remove-islands")
    if fill_holes_flag:
        cargs.append("--fill-holes")
    if noverbose_flag:
        cargs.append("--noverbose")
    if debug_flag:
        cargs.append("--debug")
    ret = MriBinarizeOutputs(
        root=execution.output_file("."),
        out_volume=execution.output_file(output_volume),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_BINARIZE_METADATA",
    "MriBinarizeOutputs",
    "mri_binarize",
]
