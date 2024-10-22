# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

LABELS_INTERSECT_METADATA = Metadata(
    id="178b5231cddc65409f78e3f5fb2fab877a5c3a4b.boutiques",
    name="labels_intersect",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class LabelsIntersectOutputs(typing.NamedTuple):
    """
    Output object returned when calling `labels_intersect(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_label: OutputPathType
    """The resulting intersected label file"""


def labels_intersect(
    label1: InputPathType,
    label2: InputPathType,
    outputname: str,
    runner: Runner | None = None,
) -> LabelsIntersectOutputs:
    """
    Tool to find the intersection of two label files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        label1: First input label file.
        label2: Second input label file.
        outputname: Output label file name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `LabelsIntersectOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LABELS_INTERSECT_METADATA)
    cargs = []
    cargs.append("/usr/local/freesurfer/bin/labels_intersect")
    cargs.append(execution.input_file(label1))
    cargs.append(execution.input_file(label2))
    cargs.append(outputname)
    ret = LabelsIntersectOutputs(
        root=execution.output_file("."),
        output_label=execution.output_file(outputname),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "LABELS_INTERSECT_METADATA",
    "LabelsIntersectOutputs",
    "labels_intersect",
]