# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_SEGMENT_THALAMIC_NUCLEI_DTI_CNN_METADATA = Metadata(
    id="0d6b3980cf69cb76b17660e3b5ddbf899684c85e.boutiques",
    name="mri_segment_thalamic_nuclei_dti_cnn",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriSegmentThalamicNucleiDtiCnnOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_segment_thalamic_nuclei_dti_cnn(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    segmentation_output: OutputPathType
    """Path to the segmentation output."""
    volume_csv: OutputPathType | None
    """CSV file with volumes for all structures."""
    posteriors: OutputPathType | None
    """Path to the posteriors output."""


def mri_segment_thalamic_nuclei_dti_cnn(
    t1_images: InputPathType,
    fa: InputPathType,
    v1: InputPathType,
    output: InputPathType,
    aseg: InputPathType | None = None,
    volume_output: InputPathType | None = None,
    posteriors_output: InputPathType | None = None,
    threads: float | None = None,
    force_cpu: bool = False,
    model: InputPathType | None = None,
    runner: Runner | None = None,
) -> MriSegmentThalamicNucleiDtiCnnOutputs:
    """
    Thalamic segmentation tool providing 0.7mm isotropic thalamus segmentation from
    registered T1, FA, and V1 volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        t1_images: Path to the T1 image(s) or folder containing images. These\
            must be registered to the FAs in physical coordinates.
        fa: Path to the FA image(s) or folder.
        v1: Path to the V1 image(s) or folder.
        output: Path to the segmentation output(s) or folder.
        aseg: Path to the ASEG segmentation(s) or folder. These must be\
            registered to the FAs in physical coordinates.
        volume_output: CSV file for volumes of all structures and subjects.
        posteriors_output: Path to the posteriors output(s) or folder.
        threads: Number of cores to be used. Default is 1.
        force_cpu: Enforce running with CPU rather than GPU.
        model: Path to an alternative model file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriSegmentThalamicNucleiDtiCnnOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_SEGMENT_THALAMIC_NUCLEI_DTI_CNN_METADATA)
    cargs = []
    cargs.append("mri_segment_thalamic_nuclei_dti_cnn")
    cargs.extend([
        "--t1",
        execution.input_file(t1_images)
    ])
    if aseg is not None:
        cargs.extend([
            "--aseg",
            execution.input_file(aseg)
        ])
    cargs.extend([
        "--fa",
        execution.input_file(fa)
    ])
    cargs.extend([
        "--v1",
        execution.input_file(v1)
    ])
    cargs.extend([
        "--o",
        execution.input_file(output)
    ])
    if volume_output is not None:
        cargs.extend([
            "--vol",
            execution.input_file(volume_output)
        ])
    if posteriors_output is not None:
        cargs.extend([
            "--post",
            execution.input_file(posteriors_output)
        ])
    if threads is not None:
        cargs.extend([
            "--threads",
            str(threads)
        ])
    if force_cpu:
        cargs.append("--cpu")
    if model is not None:
        cargs.extend([
            "--model",
            execution.input_file(model)
        ])
    ret = MriSegmentThalamicNucleiDtiCnnOutputs(
        root=execution.output_file("."),
        segmentation_output=execution.output_file(pathlib.Path(output).name),
        volume_csv=execution.output_file(pathlib.Path(volume_output).name) if (volume_output is not None) else None,
        posteriors=execution.output_file(pathlib.Path(posteriors_output).name) if (posteriors_output is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_SEGMENT_THALAMIC_NUCLEI_DTI_CNN_METADATA",
    "MriSegmentThalamicNucleiDtiCnnOutputs",
    "mri_segment_thalamic_nuclei_dti_cnn",
]
