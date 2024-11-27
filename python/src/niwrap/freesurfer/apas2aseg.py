# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

APAS2ASEG_METADATA = Metadata(
    id="3dc0c23b67aed06f4f6b85f8abfcfff2224cf026.boutiques",
    name="apas2aseg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class Apas2asegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `apas2aseg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_seg_file: OutputPathType | None
    """The output segmentation file resulting from the conversion process."""


def apas2aseg(
    subject: str | None = None,
    input_aparc_aseg: InputPathType | None = None,
    output_seg: str | None = "apas-aseg.mgz",
    runner: Runner | None = None,
) -> Apas2asegOutputs:
    """
    Converts aparc+aseg.mgz into aseg.mgz-like format by replacing specific cortical
    segmentations.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Subject identifier specifying the directory where the\
            subject's data is stored.
        input_aparc_aseg: Input aparc+aseg.mgz file to be converted.
        output_seg: Output file for the new segmentation (e.g., apas-aseg.mgz).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Apas2asegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(APAS2ASEG_METADATA)
    cargs = []
    cargs.append("apas2aseg")
    if subject is not None:
        cargs.extend([
            "--s",
            subject
        ])
    if input_aparc_aseg is not None:
        cargs.extend([
            "--i",
            execution.input_file(input_aparc_aseg)
        ])
    if output_seg is not None:
        cargs.extend([
            "--o",
            output_seg
        ])
    ret = Apas2asegOutputs(
        root=execution.output_file("."),
        output_seg_file=execution.output_file(output_seg) if (output_seg is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "APAS2ASEG_METADATA",
    "Apas2asegOutputs",
    "apas2aseg",
]
