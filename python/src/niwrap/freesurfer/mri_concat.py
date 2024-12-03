# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_CONCAT_METADATA = Metadata(
    id="fb2ef824b603c3920fd8a70883332abeb5fd81d4.boutiques",
    name="mri_concat",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriConcatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_concat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_concat(
    input_files: list[InputPathType],
    output_file: str,
    file_list: str | None = None,
    paired_sum: bool = False,
    paired_avg: bool = False,
    paired_diff: bool = False,
    paired_diff_norm: bool = False,
    paired_diff_norm1: bool = False,
    paired_diff_norm2: bool = False,
    norm_mean: bool = False,
    norm1: bool = False,
    matrix: InputPathType | None = None,
    frame_weight: InputPathType | None = None,
    norm_weight: bool = False,
    group_mean: float | None = None,
    combine: bool = False,
    keep_datatype: bool = False,
    abs_: bool = False,
    pos: bool = False,
    neg: bool = False,
    mean: bool = False,
    median: bool = False,
    mean_div_n: bool = False,
    sum_: bool = False,
    var: bool = False,
    std: bool = False,
    max_: bool = False,
    max_index: bool = False,
    max_index_prune: bool = False,
    max_index_add: float | None = None,
    min_: bool = False,
    replicate_times: float | None = None,
    fnorm: bool = False,
    conjunction: bool = False,
    vote: bool = False,
    sort: bool = False,
    temporal_ar1: float | None = None,
    prune: bool = False,
    pca: bool = False,
    pca_mask: InputPathType | None = None,
    scm: bool = False,
    zconcat: str | None = None,
    max_bonfcor: bool = False,
    multiply: float | None = None,
    add: float | None = None,
    mask_file: InputPathType | None = None,
    rms: bool = False,
    no_check: bool = False,
    runner: Runner | None = None,
) -> MriConcatOutputs:
    """
    Concatenates input data sets.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_files: Input image files (e.g. file1.mgh file2.mgh ...).
        output_file: Output file name (e.g. output.mgh).
        file_list: List file containing a text list of files to process (up to\
            400000 files).
        paired_sum: Compute paired sum (1+2, 3+4, etc).
        paired_avg: Compute paired average (1+2, 3+4, etc).
        paired_diff: Compute paired difference (1-2, 3-4, etc).
        paired_diff_norm: Compute paired difference normalized by TP1,2\
            average.
        paired_diff_norm1: Compute paired difference normalized by TP1.
        paired_diff_norm2: Compute paired difference normalized by TP2.
        norm_mean: Normalize frames by mean of all time points.
        norm1: Normalize frames by first time point (TP1).
        matrix: Multiply by matrix from ASCII file.
        frame_weight: Weight each frame by values in ASCII file (one value per\
            frame).
        norm_weight: Normalize frames to sum to 1 after weighting.
        group_mean: Create matrix to average Ng groups, Nper=Ntot/Ng.
        combine: Average frames from non-zero voxels.
        keep_datatype: Write output in the same datatype as input (default is\
            Float format).
        abs_: Take absolute value of input.
        pos: Set input negatives to 0.
        neg: Set input positives to 0.
        mean: Compute mean of concatenated volumes.
        median: Compute median of concatenated volumes.
        mean_div_n: Compute mean divided by number of frames.
        sum_: Compute sum of concatenated volumes.
        var: Compute variance of concatenated volumes.
        std: Compute standard deviation of concatenated volumes.
        max_: Compute maximum of concatenated volumes.
        max_index: Compute index of maximum of concatenated volumes.
        max_index_prune: Set max index to 0 where all frames are 0.
        max_index_add: Add value to non-zero max indices.
        min_: Compute minimum of concatenated volumes.
        replicate_times: Replicate N times over frames.
        fnorm: Normalize time series at each voxel.
        conjunction: Compute voxel-wise conjunction of concatenated volumes.
        vote: Most frequent value at each voxel and fraction of occurrences.
        sort: Sort each voxel by ascending frame value.
        temporal_ar1: Compute temporal AR1 with degree of freedom adjustment.
        prune: Set voxel value to 0 unless all frames are non-zero.
        pca: Compute and output principal component analysis (PCA).
        pca_mask: Mask used to select voxels for PCA (mask > 0.5).
        scm: Compute spatial covariance matrix.
        zconcat: Concatenate in slice direction skipping nskip slices.
        max_bonfcor: Compute maximum and Bonferroni correct.
        multiply: Multiply volumes by value.
        add: Add value to volumes.
        mask_file: Mask file used with vote or sort.
        rms: Compute root mean square of concatenated volumes.
        no_check: Do not check inputs.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriConcatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_CONCAT_METADATA)
    cargs = []
    cargs.append("mri_concat")
    cargs.extend([execution.input_file(f) for f in input_files])
    cargs.extend([
        "--o",
        output_file
    ])
    if file_list is not None:
        cargs.extend([
            "--f",
            file_list
        ])
    if paired_sum:
        cargs.append("--paired-sum")
    if paired_avg:
        cargs.append("--paired-avg")
    if paired_diff:
        cargs.append("--paired-diff")
    if paired_diff_norm:
        cargs.append("--paired-diff-norm")
    if paired_diff_norm1:
        cargs.append("--paired-diff-norm1")
    if paired_diff_norm2:
        cargs.append("--paired-diff-norm2")
    if norm_mean:
        cargs.append("--norm-mean")
    if norm1:
        cargs.append("--norm1")
    if matrix is not None:
        cargs.extend([
            "--mtx",
            execution.input_file(matrix)
        ])
    if frame_weight is not None:
        cargs.extend([
            "--w",
            execution.input_file(frame_weight)
        ])
    if norm_weight:
        cargs.append("--wn")
    if group_mean is not None:
        cargs.extend([
            "--gmean",
            str(group_mean)
        ])
    if combine:
        cargs.append("--combine")
    if keep_datatype:
        cargs.append("--keep-datatype")
    if abs_:
        cargs.append("--abs")
    if pos:
        cargs.append("--pos")
    if neg:
        cargs.append("--neg")
    if mean:
        cargs.append("--mean")
    if median:
        cargs.append("--median")
    if mean_div_n:
        cargs.append("--mean-div-n")
    if sum_:
        cargs.append("--sum")
    if var:
        cargs.append("--var")
    if std:
        cargs.append("--std")
    if max_:
        cargs.append("--max")
    if max_index:
        cargs.append("--max-index")
    if max_index_prune:
        cargs.append("--max-index-prune")
    if max_index_add is not None:
        cargs.extend([
            "--max-index-add",
            str(max_index_add)
        ])
    if min_:
        cargs.append("--min")
    if replicate_times is not None:
        cargs.extend([
            "--rep",
            str(replicate_times)
        ])
    if fnorm:
        cargs.append("--fnorm")
    if conjunction:
        cargs.append("--conjunct")
    if vote:
        cargs.append("--vote")
    if sort:
        cargs.append("--sort")
    if temporal_ar1 is not None:
        cargs.extend([
            "--tar1",
            str(temporal_ar1)
        ])
    if prune:
        cargs.append("--prune")
    if pca:
        cargs.append("--pca")
    if pca_mask is not None:
        cargs.extend([
            "--pca-mask",
            execution.input_file(pca_mask)
        ])
    if scm:
        cargs.append("--scm")
    if zconcat is not None:
        cargs.extend([
            "--zconcat",
            zconcat
        ])
    if max_bonfcor:
        cargs.append("--max-bonfcor")
    if multiply is not None:
        cargs.extend([
            "--mul",
            str(multiply)
        ])
    if add is not None:
        cargs.extend([
            "--add",
            str(add)
        ])
    if mask_file is not None:
        cargs.extend([
            "--mask",
            execution.input_file(mask_file)
        ])
    if rms:
        cargs.append("--rms")
    if no_check:
        cargs.append("--no-check")
    ret = MriConcatOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_CONCAT_METADATA",
    "MriConcatOutputs",
    "mri_concat",
]