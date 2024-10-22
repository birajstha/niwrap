# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SLICESDIR_METADATA = Metadata(
    id="f9f4f4713d5e38cd7a81f0e511839ec4001a5b5d.boutiques",
    name="slicesdir",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class SlicesdirOutputs(typing.NamedTuple):
    """
    Output object returned when calling `slicesdir(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def slicesdir(
    filelist: list[str],
    flag_filelist: bool = False,
    outline_image: InputPathType | None = None,
    edge_threshold: float | None = None,
    slice_option: bool = False,
    runner: Runner | None = None,
) -> SlicesdirOutputs:
    """
    slicesdir generates a directory containing orthogonal slices through a set of
    images.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        filelist: List of image files to process.
        flag_filelist: Filelist contains pairs of images (underlying and\
            red-outline images).
        outline_image: Use the specified image as the red-outline image on top\
            of all images in the file list.
        edge_threshold: Use specified threshold for edges. If >0, use this\
            proportion of max-min; if <0, use the absolute value.
        slice_option: Output every second axial slice instead of 9 ortho slices.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SlicesdirOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SLICESDIR_METADATA)
    cargs = []
    cargs.append("slicesdir")
    if flag_filelist:
        cargs.append("-o")
    if outline_image is not None:
        cargs.extend([
            "-p",
            execution.input_file(outline_image)
        ])
    if edge_threshold is not None:
        cargs.extend([
            "-e",
            str(edge_threshold)
        ])
    if slice_option:
        cargs.append("-S")
    cargs.extend(filelist)
    ret = SlicesdirOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SLICESDIR_METADATA",
    "SlicesdirOutputs",
    "slicesdir",
]
