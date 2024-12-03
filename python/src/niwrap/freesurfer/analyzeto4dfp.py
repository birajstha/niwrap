# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ANALYZETO4DFP_METADATA = Metadata(
    id="68ba555395398681b7b2f785a91ccbac22cbddc9.boutiques",
    name="analyzeto4dfp",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class Analyzeto4dfpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `analyzeto4dfp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def analyzeto4dfp(
    analyze_image: InputPathType,
    rois_scale: bool = False,
    flip_x: bool = False,
    flip_y: bool = False,
    flip_z: bool = False,
    endian: str | None = None,
    orientation: int | None = None,
    runner: Runner | None = None,
) -> Analyzeto4dfpOutputs:
    """
    Convert ANALYZE image format to 4dfp format with various options.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        analyze_image: Input ANALYZE image file.
        rois_scale: Apply ROIScaleFactor.
        flip_x: Flip first axis.
        flip_y: Flip second axis.
        flip_z: Flip third axis.
        endian: Output big or little endian (default CPU endian).
        orientation: Supply orientation code (in range [0-5]).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Analyzeto4dfpOutputs`).
    """
    if orientation is not None and not (0 <= orientation <= 5): 
        raise ValueError(f"'orientation' must be between 0 <= x <= 5 but was {orientation}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANALYZETO4DFP_METADATA)
    cargs = []
    cargs.append("analyzeto4dfp")
    cargs.append(execution.input_file(analyze_image))
    if rois_scale:
        cargs.append("-s")
    if flip_x:
        cargs.append("-x")
    if flip_y:
        cargs.append("-y")
    if flip_z:
        cargs.append("-z")
    if endian is not None:
        cargs.extend([
            "-@",
            endian
        ])
    if orientation is not None:
        cargs.extend([
            "-O",
            str(orientation)
        ])
    ret = Analyzeto4dfpOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ANALYZETO4DFP_METADATA",
    "Analyzeto4dfpOutputs",
    "analyzeto4dfp",
]