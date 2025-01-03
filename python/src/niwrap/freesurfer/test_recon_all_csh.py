# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TEST_RECON_ALL_CSH_METADATA = Metadata(
    id="8cf72a95ce1a11314c60b7ef805c1a1b7bf68cfb.boutiques",
    name="test_recon-all.csh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class TestReconAllCshOutputs(typing.NamedTuple):
    """
    Output object returned when calling `test_recon_all_csh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    recon_all_output: OutputPathType
    """Output from the recon-all utility."""
    mri_diff_output: OutputPathType
    """Output from the mri_diff utility."""
    mri_compute_seg_overlap_output: OutputPathType
    """Output from the mri_compute_seg_overlap utility."""
    mris_diff_output: OutputPathType
    """Output from the mris_diff utility."""
    mri_surf2surf_output: OutputPathType
    """Output from the mri_surf2surf utility."""
    mris_compute_parc_overlap_output: OutputPathType
    """Output from the mris_compute_parc_overlap utility."""
    diff_output: OutputPathType
    """Output from the diff utility."""
    asegstatsdiff_output: OutputPathType
    """Output from the asegstatsdiff utility."""
    aparcstatsdiff_output: OutputPathType
    """Output from the aparcstatsdiff utility."""


def test_recon_all_csh(
    reference_subj_source_dir: str | None = "/space/freesurfer/subjects/test/weekly_test/subjects/x86_64",
    reference_subjid: str | None = "bert",
    test_subject_dest_dir: str | None = "/tmp",
    test_subjid: str | None = "bert",
    freesurfer_home: str | None = "/usr/local/freesurfer/stable",
    norecon: bool = False,
    runner: Runner | None = None,
) -> TestReconAllCshOutputs:
    """
    Script for testing recon-all and other utilities with FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        reference_subj_source_dir: Directory of the reference subject source.
        reference_subjid: ID of the reference subject.
        test_subject_dest_dir: Directory for the test subject destination.
        test_subjid: ID of the test subject.
        freesurfer_home: Path to the FreeSurfer installation directory.
        norecon: Flag to indicate that recon-all should not be run.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TestReconAllCshOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TEST_RECON_ALL_CSH_METADATA)
    cargs = []
    cargs.append("test_recon-all.csh")
    if reference_subj_source_dir is not None:
        cargs.extend([
            "-rsd",
            reference_subj_source_dir
        ])
    if reference_subjid is not None:
        cargs.extend([
            "-rs",
            reference_subjid
        ])
    if test_subject_dest_dir is not None:
        cargs.extend([
            "-tsd",
            test_subject_dest_dir
        ])
    if test_subjid is not None:
        cargs.extend([
            "-ts",
            test_subjid
        ])
    if freesurfer_home is not None:
        cargs.extend([
            "-fshome",
            freesurfer_home
        ])
    if norecon:
        cargs.append("-norecon")
    ret = TestReconAllCshOutputs(
        root=execution.output_file("."),
        recon_all_output=execution.output_file("recon_all_output.txt"),
        mri_diff_output=execution.output_file("mri_diff_output.txt"),
        mri_compute_seg_overlap_output=execution.output_file("mri_compute_seg_overlap_output.txt"),
        mris_diff_output=execution.output_file("mris_diff_output.txt"),
        mri_surf2surf_output=execution.output_file("mri_surf2surf_output.txt"),
        mris_compute_parc_overlap_output=execution.output_file("mris_compute_parc_overlap_output.txt"),
        diff_output=execution.output_file("diff_output.txt"),
        asegstatsdiff_output=execution.output_file("asegstatsdiff_output.txt"),
        aparcstatsdiff_output=execution.output_file("aparcstatsdiff_output.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TEST_RECON_ALL_CSH_METADATA",
    "TestReconAllCshOutputs",
    "test_recon_all_csh",
]
