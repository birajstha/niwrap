# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_APARC2WMSEG_METADATA = Metadata(
    id="c2e9c2849e05b5f380308de9898034c3b156e9af.boutiques",
    name="mri_aparc2wmseg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriAparc2wmsegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_aparc2wmseg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_aparc2wmseg(
    subject: str,
    wmseg_file: str,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MriAparc2wmsegOutputs:
    """
    A tool to convert aparc+aseg.mgz annotations into a white matter segmentation
    file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: The subject identifier used in FreeSurfer.
        wmseg_file: File to store the output white matter segmentation.
        help_: Print out information on how to use this program.
        version: Print out version and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriAparc2wmsegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_APARC2WMSEG_METADATA)
    cargs = []
    cargs.append("/usr/local/freesurfer/bin/mri_aparc2wmseg")
    cargs.append("--s")
    cargs.extend([
        "--s",
        subject
    ])
    cargs.append("--wmseg")
    cargs.extend([
        "--wmseg",
        wmseg_file
    ])
    if help_:
        cargs.append("--help")
    if version:
        cargs.append("--version")
    ret = MriAparc2wmsegOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_APARC2WMSEG_METADATA",
    "MriAparc2wmsegOutputs",
    "mri_aparc2wmseg",
]