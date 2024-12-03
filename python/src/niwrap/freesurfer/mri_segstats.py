# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_SEGSTATS_METADATA = Metadata(
    id="de1b9dfa3f1dac83d5a96b745b8f327109cb07d4.boutiques",
    name="mri_segstats",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriSegstatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_segstats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    summary_output_file: OutputPathType
    """Output file for summary statistics."""
    avg_waveform_output: OutputPathType | None
    """Average waveform output text file."""
    sum_waveform_output: OutputPathType | None
    """Sum waveform output text file."""
    avg_waveform_vol_output: OutputPathType | None
    """Average waveform volume output file."""
    spatial_frame_avg_output: OutputPathType | None
    """Spatial frame average output file."""
    ctab_output_file: OutputPathType | None
    """Output color table with the reported segmentations."""


def mri_segstats(
    segvol: InputPathType,
    output_file: str,
    annot_subject: str | None = None,
    annot_hemisphere: str | None = None,
    annot_parcellation: str | None = None,
    slabel_subject: str | None = None,
    slabel_hemisphere: str | None = None,
    slabel_label: InputPathType | None = None,
    partial_vol_comp: InputPathType | None = None,
    input_volume: InputPathType | None = None,
    seg_erode: float | None = None,
    frame: float | None = None,
    robust: float | None = None,
    square_input: bool = False,
    sqrt_input: bool = False,
    multiply_input: float | None = None,
    divide_input: float | None = None,
    snr_column: bool = False,
    absolute_value: bool = False,
    accumulate_mean: bool = False,
    color_table: InputPathType | None = None,
    default_color_table: bool = False,
    gca_color_table: InputPathType | None = None,
    ids: str | None = None,
    exclude_ids: str | None = None,
    exclude_gm_wm: bool = False,
    surf_wm_vol: bool = False,
    surf_ctx_vol: bool = False,
    no_global_stats: bool = False,
    empty_segments: bool = False,
    ctab_output: str | None = None,
    mask_volume: InputPathType | None = None,
    mask_threshold: float | None = None,
    mask_sign: str | None = None,
    mask_frame: float | None = None,
    invert_mask: bool = False,
    mask_erode: float | None = None,
    brain_vol_seg: bool = False,
    brain_mask_vol: InputPathType | None = None,
    subcortical_gray: bool = False,
    total_gray: bool = False,
    intracranial_volume: bool = False,
    intracranial_volume_only: bool = False,
    old_intracranial_volume_only: bool = False,
    talairach_transform: InputPathType | None = None,
    xfm_to_etiv: str | None = None,
    euler_hole_count: bool = False,
    avg_waveform: str | None = None,
    sum_waveform: str | None = None,
    avg_waveform_vol: str | None = None,
    remove_avgwf_mean: bool = False,
    spatial_frame_avg: str | None = None,
    voxel_crs: str | None = None,
    replace_ids: str | None = None,
    replace_ids_file: InputPathType | None = None,
    gtm_default_seg_merge: bool = False,
    gtm_default_seg_merge_choroid: bool = False,
    qa_stats_file: str | None = None,
    subjects_dir: str | None = None,
    random_seed: float | None = None,
    runner: Runner | None = None,
) -> MriSegstatsOutputs:
    """
    Calculates measures and stats derived from brain segmentation data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        segvol: Input segmentation volume. This volume's voxel values indicate\
            a segmentation or class.
        output_file: ASCII file in which summary statistics are saved.
        annot_subject: Create a segmentation from hemi.parc.annot. Subject is\
            the name of the subject.
        annot_hemisphere:.
        annot_parcellation:.
        slabel_subject: Create a segmentation from the given surface label. The\
            points in the label are given a value of 1; 0 for outside.
        slabel_hemisphere:.
        slabel_label:.
        partial_vol_comp: Use pvvol to compensate for partial voluming,\
            resulting in more accurate volumes.
        input_volume: Input volume from which to compute more statistics.
        seg_erode: Erode segmentation boundaries by Nerodes.
        frame: Report statistics of the input volume at the specified 0-based\
            frame number.
        robust: Compute stats after excluding a percentage of high and low\
            values.
        square_input: Compute the square of the input before computing stats.
        sqrt_input: Compute the square root of the input before computing\
            stats.
        multiply_input: Multiply input by value.
        divide_input: Divide input by value.
        snr_column: Save mean/std as extra column in output table.
        absolute_value: Compute absolute value of input before spatial average.
        accumulate_mean: Save mean*nvoxels instead of mean.
        color_table: FreeSurfer color table file to specify how each\
            segmentation index is mapped to a segmentation name and color.
        default_color_table: Use default color table from\
            FreeSurferColorLUT.txt.
        gca_color_table: Get color table from the given GCA file.
        ids: Specify numeric segmentation ids.
        exclude_ids: Exclude the given segmentation id(s) from report.
        exclude_gm_wm: Exclude cortical gray and white matter based on\
            predefined IDs.
        surf_wm_vol: Compute cortical matter volume based on the white surface\
            volume.
        surf_ctx_vol: Compute cortical volumes from surface.
        no_global_stats: Turns off computation of global stats.
        empty_segments: Report on segmentations listed in the color table even\
            if they are not found in the segmentation volume.
        ctab_output: Create an output color table with just the segmentations\
            reported.
        mask_volume: Exclude voxels that are not in the mask. Voxels to be\
            excluded are assigned a segid of 0.
        mask_threshold: Exclude voxels that are below thresh, above -thresh, or\
            between -thresh and +thresh.
        mask_sign: Specify sign for masking threshold. Choices are abs, pos,\
            and neg.
        mask_frame: Derive the mask volume from the specified 0-based frame.
        invert_mask: After applying all the masking criteria, invert the mask.
        mask_erode: Erode mask by specified number of iterations.
        brain_vol_seg: Get volume of brain as the sum of the volumes of the\
            segmentations that are in the brain.
        brain_mask_vol: Load brain mask and compute brain volume from non-zero\
            voxels.
        subcortical_gray: Compute volume of subcortical gray matter.
        total_gray: Compute volume of total gray matter.
        intracranial_volume: Compute intracranial volume from talairach.xfm.
        intracranial_volume_only: Compute intracranial volume from\
            talairach.xfm and exit.
        old_intracranial_volume_only: Compute intracranial volume from\
            talairach_with_skull.lta and exit.
        talairach_transform: Specify path to talairach.xfm file for eTIV.
        xfm_to_etiv: Convert xfm to eTIV and write to output file.
        euler_hole_count: Write out number of defect holes based on the Euler\
            number.
        avg_waveform: Compute the average waveform and save to text file.
        sum_waveform: Compute the sum waveform and save to text file.
        avg_waveform_vol: Compute average waveform and save to MRI volume.
        remove_avgwf_mean: Remove temporal mean from avgwf and avgwfvol.
        spatial_frame_avg: Save mean across space and frame.
        voxel_crs: Replace segmentation with all 0s except at specified voxel.
        replace_ids: Replace segmentation ID1 with ID2.
        replace_ids_file: Replace segmentations based on pairs in file.
        gtm_default_seg_merge: Replace segmentations based on GTM default.
        gtm_default_seg_merge_choroid: Replace segmentations based on GTM\
            default excluding choroid.
        qa_stats_file: Compute stats useful for quality control.
        subjects_dir: Set SUBJECTS_DIR environment variable.
        random_seed: Set random number generator seed value.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriSegstatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_SEGSTATS_METADATA)
    cargs = []
    cargs.append("mri_segstats")
    cargs.extend([
        "--seg",
        execution.input_file(segvol)
    ])
    if annot_subject is not None:
        cargs.extend([
            "--annot",
            annot_subject
        ])
    if annot_hemisphere is not None:
        cargs.append(annot_hemisphere)
    if annot_parcellation is not None:
        cargs.append(annot_parcellation)
    if slabel_subject is not None:
        cargs.extend([
            "--slabel",
            slabel_subject
        ])
    if slabel_hemisphere is not None:
        cargs.append(slabel_hemisphere)
    if slabel_label is not None:
        cargs.append(execution.input_file(slabel_label))
    cargs.extend([
        "--o",
        output_file
    ])
    if partial_vol_comp is not None:
        cargs.extend([
            "--pv",
            execution.input_file(partial_vol_comp)
        ])
    if input_volume is not None:
        cargs.extend([
            "--i",
            execution.input_file(input_volume)
        ])
    if seg_erode is not None:
        cargs.extend([
            "--seg-erode",
            str(seg_erode)
        ])
    if frame is not None:
        cargs.extend([
            "--frame",
            str(frame)
        ])
    if robust is not None:
        cargs.extend([
            "--robust",
            str(robust)
        ])
    if square_input:
        cargs.append("--sqr")
    if sqrt_input:
        cargs.append("--sqrt")
    if multiply_input is not None:
        cargs.extend([
            "--mul",
            str(multiply_input)
        ])
    if divide_input is not None:
        cargs.extend([
            "--div",
            str(divide_input)
        ])
    if snr_column:
        cargs.append("--snr")
    if absolute_value:
        cargs.append("--abs")
    if accumulate_mean:
        cargs.append("--accumulate")
    if color_table is not None:
        cargs.extend([
            "--ctab",
            execution.input_file(color_table)
        ])
    if default_color_table:
        cargs.append("--ctab-default")
    if gca_color_table is not None:
        cargs.extend([
            "--ctab-gca",
            execution.input_file(gca_color_table)
        ])
    if ids is not None:
        cargs.extend([
            "--id",
            ids
        ])
    if exclude_ids is not None:
        cargs.extend([
            "--excludeid",
            exclude_ids
        ])
    if exclude_gm_wm:
        cargs.append("--excl-ctxgmwm")
    if surf_wm_vol:
        cargs.append("--surf-wm-vol")
    if surf_ctx_vol:
        cargs.append("--surf-ctx-vol")
    if no_global_stats:
        cargs.append("--no-global-stats")
    if empty_segments:
        cargs.append("--empty")
    if ctab_output is not None:
        cargs.extend([
            "--ctab-out",
            ctab_output
        ])
    if mask_volume is not None:
        cargs.extend([
            "--mask",
            execution.input_file(mask_volume)
        ])
    if mask_threshold is not None:
        cargs.extend([
            "--maskthresh",
            str(mask_threshold)
        ])
    if mask_sign is not None:
        cargs.extend([
            "--masksign",
            mask_sign
        ])
    if mask_frame is not None:
        cargs.extend([
            "--maskframe",
            str(mask_frame)
        ])
    if invert_mask:
        cargs.append("--maskinvert")
    if mask_erode is not None:
        cargs.extend([
            "--maskerode",
            str(mask_erode)
        ])
    if brain_vol_seg:
        cargs.append("--brain-vol-from-seg")
    if brain_mask_vol is not None:
        cargs.extend([
            "--brainmask",
            execution.input_file(brain_mask_vol)
        ])
    if subcortical_gray:
        cargs.append("--subcortgray")
    if total_gray:
        cargs.append("--totalgray")
    if intracranial_volume:
        cargs.append("--etiv")
    if intracranial_volume_only:
        cargs.append("--etiv-only")
    if old_intracranial_volume_only:
        cargs.append("--old-etiv-only")
    if talairach_transform is not None:
        cargs.extend([
            "--talxfm",
            execution.input_file(talairach_transform)
        ])
    if xfm_to_etiv is not None:
        cargs.extend([
            "--xfm2etiv",
            xfm_to_etiv
        ])
    if euler_hole_count:
        cargs.append("--euler")
    if avg_waveform is not None:
        cargs.extend([
            "--avgwf",
            avg_waveform
        ])
    if sum_waveform is not None:
        cargs.extend([
            "--sumwf",
            sum_waveform
        ])
    if avg_waveform_vol is not None:
        cargs.extend([
            "--avgwfvol",
            avg_waveform_vol
        ])
    if remove_avgwf_mean:
        cargs.append("--avgwf-remove-mean")
    if spatial_frame_avg is not None:
        cargs.extend([
            "--sfavg",
            spatial_frame_avg
        ])
    if voxel_crs is not None:
        cargs.extend([
            "--vox",
            voxel_crs
        ])
    if replace_ids is not None:
        cargs.extend([
            "--replace",
            replace_ids
        ])
    if replace_ids_file is not None:
        cargs.extend([
            "--replace-file",
            execution.input_file(replace_ids_file)
        ])
    if gtm_default_seg_merge:
        cargs.append("--gtm-default-seg-merge")
    if gtm_default_seg_merge_choroid:
        cargs.append("--gtm-default-seg-merge-choroid")
    if qa_stats_file is not None:
        cargs.extend([
            "--qa-stats",
            qa_stats_file
        ])
    if subjects_dir is not None:
        cargs.extend([
            "--sd",
            subjects_dir
        ])
    if random_seed is not None:
        cargs.extend([
            "--seed",
            str(random_seed)
        ])
    ret = MriSegstatsOutputs(
        root=execution.output_file("."),
        summary_output_file=execution.output_file(output_file),
        avg_waveform_output=execution.output_file(avg_waveform) if (avg_waveform is not None) else None,
        sum_waveform_output=execution.output_file(sum_waveform) if (sum_waveform is not None) else None,
        avg_waveform_vol_output=execution.output_file(avg_waveform_vol) if (avg_waveform_vol is not None) else None,
        spatial_frame_avg_output=execution.output_file(spatial_frame_avg) if (spatial_frame_avg is not None) else None,
        ctab_output_file=execution.output_file(ctab_output) if (ctab_output is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_SEGSTATS_METADATA",
    "MriSegstatsOutputs",
    "mri_segstats",
]