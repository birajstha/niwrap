# This file was auto generated by Styx.
# Do not edit this file directly.

import pathlib
import typing

from styxdefs import *


VOLUME_REMOVE_ISLANDS_METADATA = Metadata(
    id="8da548798edf32ac1baff399a00bbd659acf8ddb",
    name="volume-remove-islands",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
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
    volume_out: InputPathType,
    runner: Runner = None,
) -> VolumeRemoveIslandsOutputs:
    """
    volume-remove-islands by Washington University School of Medicin.
    
    Remove islands from an roi volume.
    
    Finds all face-connected parts of the ROI, and zeros out all but the largest
    one.
    
    Args:
        volume_in: the input ROI volume
        volume_out: the output ROI volume
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `VolumeRemoveIslandsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_REMOVE_ISLANDS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-remove-islands")
    cargs.append(execution.input_file(volume_in))
    cargs.append(execution.input_file(volume_out))
    ret = VolumeRemoveIslandsOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(f"{pathlib.Path(volume_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_REMOVE_ISLANDS_METADATA",
    "VolumeRemoveIslandsOutputs",
    "volume_remove_islands",
]
