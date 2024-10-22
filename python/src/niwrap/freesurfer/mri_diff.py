# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_DIFF_METADATA = Metadata(
    id="7af6221ce1f32e851c0a61a25905ed0002e319bd.boutiques",
    name="mri_diff",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriDiffOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_diff(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    log_output: OutputPathType | None
    """Log file containing difference information."""
    difference_image_output: OutputPathType | None
    """Difference image output file."""
    suspicious_difference_output: OutputPathType | None
    """Volume with suspicious differences labeled."""


def mri_diff(
    vol1file: InputPathType,
    vol2file: InputPathType,
    resolution_check: bool = False,
    acquisition_param_check: bool = False,
    geometry_check: bool = False,
    precision_check: bool = False,
    pixel_check: bool = False,
    orientation_check: bool = False,
    file_type_diff_check: bool = False,
    no_exit_on_diff: bool = False,
    quality_assurance: bool = False,
    pixel_only: bool = False,
    abs_difference: bool = False,
    no_abs_difference: bool = False,
    difference_abs: bool = False,
    percentage_difference: bool = False,
    rss_save: bool = False,
    ssd_print: bool = False,
    rms_print: bool = False,
    count_diff_voxels: bool = False,
    pixel_threshold: float | None = None,
    count_thresh_voxels: float | None = None,
    log_file: str | None = None,
    difference_image: InputPathType | None = None,
    suspicious_diff_volume: InputPathType | None = None,
    segmentation_diff: str | None = None,
    merge_edits: str | None = None,
    average_difference: str | None = None,
    debug_mode: bool = False,
    verbose_mode: bool = False,
    check_options: bool = False,
    runner: Runner | None = None,
) -> MriDiffOutputs:
    """
    Determines whether two volumes differ based on dimensions, resolutions,
    acquisition parameters, geometry, precision, and pixel data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        vol1file: First volume to compare (e.g., vol1.mgz).
        vol2file: Second volume to compare (e.g., vol2.mgz).
        resolution_check: Do not check for resolution differences.
        acquisition_param_check: Do not check for acquisition parameter\
            differences.
        geometry_check: Do not check for geometry differences.
        precision_check: Do not check for precision differences.
        pixel_check: Do not check for pixel differences.
        orientation_check: Do not check for orientation differences.
        file_type_diff_check: Do not check for file type differences.
        no_exit_on_diff: Do not exit on difference; run through everything.
        quality_assurance: Check resolution, acquisition, precision, and\
            orientation only.
        pixel_only: Only check pixel data.
        abs_difference: Take absolute value of difference (default).
        no_abs_difference: Do not take absolute value of difference.
        difference_abs: Take absolute value before computing difference.
        percentage_difference: Compute percentage difference:\
            100*(v1-v2)/((v1+v2)/2).
        rss_save: Save square root sum squares with --diff.
        ssd_print: Print sum squared differences over all voxels.
        rms_print: Print root mean squared difference over all non-zero voxels.
        count_diff_voxels: Print number of differing voxels.
        pixel_threshold: Pixel differences must be greater than this value to\
            be considered different.
        count_thresh_voxels: There must be at least this many voxels that are\
            different.
        log_file: Store difference information in this log file.
        difference_image: Save difference image to specified volume.
        suspicious_diff_volume: Differing voxels replaced with label SUSPICIOUS\
            in the specified volume.
        segmentation_diff: Perform diff on voxels with specific label index.
        merge_edits: Merge edits from newauto, oldauto, and manedit volumes\
            into merged volume.
        average_difference: Save average difference to specified file.
        debug_mode: Enable debugging mode.
        verbose_mode: Print information on all differences found.
        check_options: Check options and exit without running anything.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriDiffOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_DIFF_METADATA)
    cargs = []
    cargs.append("/usr/local/freesurfer/bin/mri_diff")
    cargs.append(execution.input_file(vol1file))
    cargs.append(execution.input_file(vol2file))
    if resolution_check:
        cargs.append("--notallow-res")
    if acquisition_param_check:
        cargs.append("--notallow-acq")
    if geometry_check:
        cargs.append("--notallow-geo")
    if precision_check:
        cargs.append("--notallow-prec")
    if pixel_check:
        cargs.append("--notallow-pix")
    if orientation_check:
        cargs.append("--notallow-ori")
    if file_type_diff_check:
        cargs.append("--notallow-type")
    if no_exit_on_diff:
        cargs.append("--no-exit-on-diff")
    if quality_assurance:
        cargs.append("--qa")
    if pixel_only:
        cargs.append("--pix-only")
    if abs_difference:
        cargs.append("--absdiff")
    if no_abs_difference:
        cargs.append("--no-absdiff")
    if difference_abs:
        cargs.append("--diffabs")
    if percentage_difference:
        cargs.append("--diffpct")
    if rss_save:
        cargs.append("--rss")
    if ssd_print:
        cargs.append("--ssd")
    if rms_print:
        cargs.append("--rms")
    if count_diff_voxels:
        cargs.append("--count")
    if pixel_threshold is not None:
        cargs.extend([
            "--thresh",
            str(pixel_threshold)
        ])
    if count_thresh_voxels is not None:
        cargs.extend([
            "--count-thresh",
            str(count_thresh_voxels)
        ])
    if log_file is not None:
        cargs.extend([
            "--log",
            log_file
        ])
    if difference_image is not None:
        cargs.extend([
            "--diff",
            execution.input_file(difference_image)
        ])
    if suspicious_diff_volume is not None:
        cargs.extend([
            "--diff_label_suspicious",
            execution.input_file(suspicious_diff_volume)
        ])
    if segmentation_diff is not None:
        cargs.extend([
            "--segdiff",
            segmentation_diff
        ])
    if merge_edits is not None:
        cargs.extend([
            "--merge-edits",
            merge_edits
        ])
    if average_difference is not None:
        cargs.extend([
            "--avg-diff",
            average_difference
        ])
    if debug_mode:
        cargs.append("--debug")
    if verbose_mode:
        cargs.append("--verbose")
    if check_options:
        cargs.append("--checkopts")
    ret = MriDiffOutputs(
        root=execution.output_file("."),
        log_output=execution.output_file(log_file) if (log_file is not None) else None,
        difference_image_output=execution.output_file(pathlib.Path(difference_image).name) if (difference_image is not None) else None,
        suspicious_difference_output=execution.output_file(pathlib.Path(suspicious_diff_volume).name) if (suspicious_diff_volume is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_DIFF_METADATA",
    "MriDiffOutputs",
    "mri_diff",
]