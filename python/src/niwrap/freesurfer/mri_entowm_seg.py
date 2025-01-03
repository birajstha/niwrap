# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_ENTOWM_SEG_METADATA = Metadata(
    id="1006528a783aba45037e74965263293e175c5f7f.boutiques",
    name="mri_entowm_seg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriEntowmSegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_entowm_seg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType | None
    """Segmentation output file"""
    label_posteriors: OutputPathType | None
    """Label posterior probabilities"""
    volume_stats: OutputPathType | None
    """Volume statistics"""
    qa_stats: OutputPathType | None
    """Quality assurance statistics"""


def mri_entowm_seg(
    input_image: InputPathType | None = None,
    output_segmentation: InputPathType | None = None,
    recon_subjects: list[str] | None = None,
    subjects_directory: str | None = None,
    conform: bool = False,
    etiv: bool = False,
    tal: str | None = None,
    write_posteriors: bool = False,
    write_volumes: bool = False,
    write_qa_stats: bool = False,
    exclude_labels: list[str] | None = None,
    keep_ac: bool = False,
    vox_count_volumes: bool = False,
    model_weights: str | None = None,
    color_table: str | None = None,
    population_stats: str | None = None,
    debug: bool = False,
    vmp: bool = False,
    threads: float | None = None,
    seven_tesla: bool = False,
    percentile: float | None = None,
    cuda_device: str | None = None,
    output_base: str | None = None,
    no_cite_sclimbic: bool = False,
    nchannels: float | None = None,
    runner: Runner | None = None,
) -> MriEntowmSegOutputs:
    """
    Segment white matter near gyrus ambiens entorhinal cortex using a deep learning
    model.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_image: T1-weighted image(s) to segment. Can be a path to a single\
            image or a directory of images.
        output_segmentation: Segmentation output file or directory (required if\
            --i is provided).
        recon_subjects: Process a series of FreeSurfer recon-all subjects,\
            enables subject-mode.
        subjects_directory: Set the subjects directory, overrides the\
            SUBJECTS_DIR env variable.
        conform: Resample input to 1mm-iso; results will be put back in native\
            resolution.
        etiv: Include eTIV in volume stats (enabled by default in subject-mode\
            and with --tal).
        tal: Alternative talairach xfm transform for estimating TIV, can be\
            file or suffix (for multiple inputs).
        write_posteriors: Save the label posteriors.
        write_volumes: Save label volume stats (enabled by default in\
            subject-mode).
        write_qa_stats: Save QA stats (z and confidence).
        exclude_labels: List of label IDs to exclude in any output stats files.
        keep_ac: Explicitly keep anterior commissure in the volume/QA files.
        vox_count_volumes: Use discrete voxel count for label volumes.
        model_weights: Alternative model weights to load.
        color_table: Alternative color lookup table to embed in segmentation.\
            Must be minimal, including 0, and sorted.
        population_stats: Alternative population volume stats for QA output.
        debug: Enable debug logging.
        vmp: Enable printing of vmpeak at the end.
        threads: Number of threads to use. Default is 1.
        seven_tesla: Preprocess 7T images (just sets percentile to 99.9).
        percentile: Use intensity percentile threshold for normalization.
        cuda_device: CUDA device for GPU support.
        output_base: String to use in output file name; default is sclimbic.
        no_cite_sclimbic: Do not cite sclimbic paper at the end.
        nchannels: Number of channels.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriEntowmSegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_ENTOWM_SEG_METADATA)
    cargs = []
    cargs.append("mri_entowm_seg")
    if input_image is not None:
        cargs.extend([
            "-i",
            execution.input_file(input_image)
        ])
    if output_segmentation is not None:
        cargs.extend([
            "-o",
            execution.input_file(output_segmentation)
        ])
    if recon_subjects is not None:
        cargs.extend([
            "-s",
            *recon_subjects
        ])
    if subjects_directory is not None:
        cargs.extend([
            "--sd",
            subjects_directory
        ])
    if conform:
        cargs.append("--conform")
    if etiv:
        cargs.append("--etiv")
    if tal is not None:
        cargs.extend([
            "--tal",
            tal
        ])
    if write_posteriors:
        cargs.append("--write_posteriors")
    if write_volumes:
        cargs.append("--write_volumes")
    if write_qa_stats:
        cargs.append("--write_qa_stats")
    if exclude_labels is not None:
        cargs.extend([
            "--exclude",
            *exclude_labels
        ])
    if keep_ac:
        cargs.append("--keep_ac")
    if vox_count_volumes:
        cargs.append("--vox-count-volumes")
    if model_weights is not None:
        cargs.extend([
            "--model",
            model_weights
        ])
    if color_table is not None:
        cargs.extend([
            "--ctab",
            color_table
        ])
    if population_stats is not None:
        cargs.extend([
            "--population-stats",
            population_stats
        ])
    if debug:
        cargs.append("--debug")
    if vmp:
        cargs.append("--vmp")
    if threads is not None:
        cargs.extend([
            "--threads",
            str(threads)
        ])
    if seven_tesla:
        cargs.append("--7T")
    if percentile is not None:
        cargs.extend([
            "--percentile",
            str(percentile)
        ])
    if cuda_device is not None:
        cargs.extend([
            "--cuda-device",
            cuda_device
        ])
    if output_base is not None:
        cargs.extend([
            "--output-base",
            output_base
        ])
    if no_cite_sclimbic:
        cargs.append("--no-cite-sclimbic")
    if nchannels is not None:
        cargs.extend([
            "--nchannels",
            str(nchannels)
        ])
    ret = MriEntowmSegOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(pathlib.Path(output_segmentation).name) if (output_segmentation is not None) else None,
        label_posteriors=execution.output_file(output_base + "_posterior.mgz") if (output_base is not None) else None,
        volume_stats=execution.output_file(output_base + "_volumes.txt") if (output_base is not None) else None,
        qa_stats=execution.output_file(output_base + "_qa_stats.txt") if (output_base is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_ENTOWM_SEG_METADATA",
    "MriEntowmSegOutputs",
    "mri_entowm_seg",
]
