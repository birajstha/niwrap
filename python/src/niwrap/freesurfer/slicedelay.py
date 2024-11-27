# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SLICEDELAY_METADATA = Metadata(
    id="a9d3a1fdb81dcd7330d4aa6bdd422c6e9cedddd8.boutiques",
    name="slicedelay",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class SlicedelayOutputs(typing.NamedTuple):
    """
    Output object returned when calling `slicedelay(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    slicedelayfile: OutputPathType
    """The generated slice delay file"""


def slicedelay(
    slicedelayfile: str,
    nslices: float,
    order: typing.Literal["up", "down", "odd", "even", "siemens"],
    ngroups: float,
    runner: Runner | None = None,
) -> SlicedelayOutputs:
    """
    Creates an FSL custom slice delay file for use with slicetimer for slice-time
    correction of fMRI.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        slicedelayfile: Output file for the custom slice delay.
        nslices: Total number of slices in the volume.
        order: Order of slices (up, down, odd, even, siemens).
        ngroups: Number of slice groups for SMS.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SlicedelayOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SLICEDELAY_METADATA)
    cargs = []
    cargs.append("slicedelay")
    cargs.extend([
        "--o",
        slicedelayfile
    ])
    cargs.extend([
        "--nslices",
        str(nslices)
    ])
    cargs.extend([
        "--order",
        order
    ])
    cargs.extend([
        "--ngroups",
        str(ngroups)
    ])
    ret = SlicedelayOutputs(
        root=execution.output_file("."),
        slicedelayfile=execution.output_file("[SLICE_DELAY_FILE]"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SLICEDELAY_METADATA",
    "SlicedelayOutputs",
    "slicedelay",
]
