# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_SEG_OVERLAP_METADATA = Metadata(
    id="e61800f776c2289b9b4a7391243b109288f38e81.boutiques",
    name="mri_seg_overlap",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriSegOverlapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_seg_overlap(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    overlap_report: OutputPathType | None
    """Detailed overlap report saved to a JSON file."""


def mri_seg_overlap(
    vol1: InputPathType,
    vol2: InputPathType,
    out_file: str | None = None,
    measures: list[str] | None = None,
    labels: list[str] | None = None,
    label_names: list[str] | None = None,
    label_file: InputPathType | None = None,
    no_names_flag: bool = False,
    seg_flag: bool = False,
    quiet_flag: bool = False,
    runner: Runner | None = None,
) -> MriSegOverlapOutputs:
    """
    Compute the structural overlap between two segmentation volumes.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        vol1: First segmentation volume input.
        vol2: Second segmentation volume input.
        out_file: Save detailed overlap report to a JSON file.
        measures: List of measures to compute. Options include: dice, jaccard,\
            voldiff.
        labels: Space-separated list of label values to include.
        label_names: Custom label names corresponding to the values specified\
            with the --labels flag.
        label_file: Text file specifying the label values to include. Must be\
            in the format of a freesurfer lookup-table.
        no_names_flag: Do not report label names.
        seg_flag: Compute overlap between the major segmentation structures.
        quiet_flag: Quiet mode - do not print results to stdout.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriSegOverlapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_SEG_OVERLAP_METADATA)
    cargs = []
    cargs.append("mri_seg_overlap")
    cargs.append(execution.input_file(vol1))
    cargs.append(execution.input_file(vol2))
    if out_file is not None:
        cargs.extend([
            "-o",
            out_file
        ])
    if measures is not None:
        cargs.extend([
            "-m",
            *measures
        ])
    if labels is not None:
        cargs.extend([
            "-l",
            *labels
        ])
    if label_names is not None:
        cargs.extend([
            "-n",
            *label_names
        ])
    if label_file is not None:
        cargs.extend([
            "-f",
            execution.input_file(label_file)
        ])
    if no_names_flag:
        cargs.append("-x")
    if seg_flag:
        cargs.append("-s")
    if quiet_flag:
        cargs.append("-q")
    ret = MriSegOverlapOutputs(
        root=execution.output_file("."),
        overlap_report=execution.output_file(out_file) if (out_file is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_SEG_OVERLAP_METADATA",
    "MriSegOverlapOutputs",
    "mri_seg_overlap",
]
