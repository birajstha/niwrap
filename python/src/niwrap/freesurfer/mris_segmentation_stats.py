# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_SEGMENTATION_STATS_METADATA = Metadata(
    id="c496c4babb272fe5cf304c7413672a6f323ade3f.boutiques",
    name="mris_segmentation_stats",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisSegmentationStatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_segmentation_stats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    roc_output_file: OutputPathType
    """ROC curve file"""


def mris_segmentation_stats(
    overlay_name: str,
    segmentation_label_name: str,
    subjects: list[str],
    roc_file: str,
    runner: Runner | None = None,
) -> MrisSegmentationStatsOutputs:
    """
    Tool for calculating segmentation statistics.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        overlay_name: Overlay name for segmentation.
        segmentation_label_name: Segmentation label name.
        subjects: List of subjects to process.
        roc_file: File for ROC curve output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisSegmentationStatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_SEGMENTATION_STATS_METADATA)
    cargs = []
    cargs.append("mris_segmentation_stats")
    cargs.append(overlay_name)
    cargs.append(segmentation_label_name)
    cargs.extend(subjects)
    cargs.append(roc_file)
    ret = MrisSegmentationStatsOutputs(
        root=execution.output_file("."),
        roc_output_file=execution.output_file(roc_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_SEGMENTATION_STATS_METADATA",
    "MrisSegmentationStatsOutputs",
    "mris_segmentation_stats",
]
