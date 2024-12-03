# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MERGESEG_METADATA = Metadata(
    id="8df8bb8db74182788b29b00177c93fd3d1402bd4.boutiques",
    name="mergeseg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MergesegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mergeseg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_seg: OutputPathType
    """Output merged segmentation result."""


def mergeseg(
    src_seg: InputPathType,
    merge_seg: InputPathType,
    out_seg: InputPathType,
    segid: float | None = None,
    segid_only: float | None = None,
    segid_erode: float | None = None,
    ctab: InputPathType | None = None,
    runner: Runner | None = None,
) -> MergesegOutputs:
    """
    Merges one segmentation into another, replacing the source voxels with those
    from the merge segmentation where non-zero.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        src_seg: Source segmentation image file.
        merge_seg: Merge segmentation volume file.
        out_seg: Output merged segmentation.
        segid: Segmentation index (optional). If specified, all the voxels in\
            the merge seg will be set to segindex.
        segid_only: Only take segindex from merge and use it for merging.
        segid_erode: Erode seg-only segindex before merge. Specify the number\
            of erosion iterations.
        ctab: Color table to embed in the output segmentation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MergesegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MERGESEG_METADATA)
    cargs = []
    cargs.append("mergeseg")
    cargs.append(execution.input_file(src_seg))
    cargs.append(execution.input_file(merge_seg))
    cargs.extend([
        "--o",
        execution.input_file(out_seg)
    ])
    if segid is not None:
        cargs.extend([
            "--segid",
            str(segid)
        ])
    if segid_only is not None:
        cargs.extend([
            "--segid-only",
            str(segid_only)
        ])
    if segid_erode is not None:
        cargs.extend([
            "--segid-erode",
            str(segid_erode)
        ])
    if ctab is not None:
        cargs.extend([
            "--ctab",
            execution.input_file(ctab)
        ])
    ret = MergesegOutputs(
        root=execution.output_file("."),
        output_seg=execution.output_file(pathlib.Path(out_seg).name),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MERGESEG_METADATA",
    "MergesegOutputs",
    "mergeseg",
]