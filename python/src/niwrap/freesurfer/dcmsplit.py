# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DCMSPLIT_METADATA = Metadata(
    id="3d5aa62fefcd13c6396a58e6fed84abe77250c1e.boutiques",
    name="dcmsplit",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class DcmsplitOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dcmsplit(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def dcmsplit(
    dcm_dir: str,
    out_dir: str,
    copy_: bool = False,
    link: bool = False,
    split_name: bool = False,
    split_uid: bool = False,
    series_no: bool = False,
    series_plus: bool = False,
    dicom_tag: str | None = None,
    study_description: bool = False,
    runner: Runner | None = None,
) -> DcmsplitOutputs:
    """
    Splits DICOM files into separate folders based on a unique identifier (UID).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        dcm_dir: Directory containing the DICOM files.
        out_dir: Output directory for split DICOM files.
        copy_: Copy files instead of creating symbolic links.
        link: Link files instead of copying (default behavior).
        split_name: Split files by patient name instead of UID.
        split_uid: Split files by Study UID instead of name (default behavior).
        series_no: Split files by series number.
        series_plus: Split files by series number and either name or UID.
        dicom_tag: Split files by given DICOM tag (group element).
        study_description: Split files by Study Description.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DcmsplitOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DCMSPLIT_METADATA)
    cargs = []
    cargs.append("dcmsplit")
    cargs.extend([
        "--dcm",
        dcm_dir
    ])
    cargs.extend([
        "--o",
        out_dir
    ])
    if copy_:
        cargs.append("--cp")
    if link:
        cargs.append("--link")
    if split_name:
        cargs.append("--name")
    if split_uid:
        cargs.append("--uid")
    if series_no:
        cargs.append("--seriesno")
    if series_plus:
        cargs.append("--series+")
    if dicom_tag is not None:
        cargs.extend([
            "--t",
            dicom_tag
        ])
    if study_description:
        cargs.append("--studyDes")
    ret = DcmsplitOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DCMSPLIT_METADATA",
    "DcmsplitOutputs",
    "dcmsplit",
]
