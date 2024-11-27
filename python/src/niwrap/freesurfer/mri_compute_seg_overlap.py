# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_COMPUTE_SEG_OVERLAP_METADATA = Metadata(
    id="6a55fd087e217296215136f8bd25bc2fa65bfb23.boutiques",
    name="mri_compute_seg_overlap",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriComputeSegOverlapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_compute_seg_overlap(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_compute_seg_overlap(
    segvol1: InputPathType,
    segvol2: InputPathType,
    log_file: str | None = None,
    mean_log_file: str | None = None,
    std_log_file: str | None = None,
    overall_log_flag: bool = False,
    exclude_cortex_flag: bool = False,
    exclude_wm_flag: bool = False,
    all_labels_flag: bool = False,
    dice_params: str | None = None,
    runner: Runner | None = None,
) -> MriComputeSegOverlapOutputs:
    """
    Compute coefficients of overlap between segmentation volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        segvol1: First segmentation volume.
        segvol2: Second segmentation volume.
        log_file: Log file for individual Dice coefficients for 12 structure\
            pairs, plus mean, std, and 'overall'.
        mean_log_file: Log file for mean Dice.
        std_log_file: Log file for std Dice.
        overall_log_flag: Log file for 'overall' Dice (mean excluding wm, gm,\
            and accumbens).
        exclude_cortex_flag: Exclude cerebral cortex labels from all\
            calculation. (0/1 flag, if nonzero).
        exclude_wm_flag: Exclude cerebral white matter labels from all\
            calculation. (0/1 flag, if nonzero).
        all_labels_flag: Check all labels, not just the predefined main\
            structures.
        dice_params: Standalone way to compute Dice coefficients, using seg1,\
            seg2, ctab, ReportEmpty01, ExcludeId, datfile, and tablefile as\
            additional parameters.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriComputeSegOverlapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_COMPUTE_SEG_OVERLAP_METADATA)
    cargs = []
    cargs.append("mri_compute_seg_overlap")
    cargs.append(execution.input_file(segvol1))
    cargs.append(execution.input_file(segvol2))
    if log_file is not None:
        cargs.extend([
            "-log",
            log_file
        ])
    if mean_log_file is not None:
        cargs.extend([
            "-mlog",
            mean_log_file
        ])
    if std_log_file is not None:
        cargs.extend([
            "-slog",
            std_log_file
        ])
    if overall_log_flag:
        cargs.append("-olog")
    if exclude_cortex_flag:
        cargs.append("-cortex")
    if exclude_wm_flag:
        cargs.append("-wm")
    if all_labels_flag:
        cargs.append("-all_labels")
    if dice_params is not None:
        cargs.extend([
            "-dice",
            dice_params
        ])
    ret = MriComputeSegOverlapOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_COMPUTE_SEG_OVERLAP_METADATA",
    "MriComputeSegOverlapOutputs",
    "mri_compute_seg_overlap",
]
