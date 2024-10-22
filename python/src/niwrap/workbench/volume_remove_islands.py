# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

VOLUME_REMOVE_ISLANDS_METADATA = Metadata(
    id="2280490d5511475f92da4664c5d1d511533b9e59.boutiques",
    name="volume-remove-islands",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


class VolumeRemoveIslandsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_remove_islands(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output ROI volume"""


def volume_remove_islands(
    volume_in: InputPathType,
    volume_out: str,
    runner: Runner | None = None,
) -> VolumeRemoveIslandsOutputs:
    """
    Remove islands from an roi volume.
    
    Finds all face-connected parts of the ROI, and zeros out all but the largest
    one.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        volume_in: the input ROI volume.
        volume_out: the output ROI volume.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeRemoveIslandsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_REMOVE_ISLANDS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-remove-islands")
    cargs.append(execution.input_file(volume_in))
    cargs.append(volume_out)
    ret = VolumeRemoveIslandsOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(volume_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_REMOVE_ISLANDS_METADATA",
    "VolumeRemoveIslandsOutputs",
    "volume_remove_islands",
]
