# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_COMPUTE_VOLUME_FRACTIONS_METADATA = Metadata(
    id="02961ba1db8b265f07c25a08461891b1caa9c54c.boutiques",
    name="mris_compute_volume_fractions",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisComputeVolumeFractionsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_compute_volume_fractions(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume_file: OutputPathType
    """The output volume file containing the computed fractions."""


def mris_compute_volume_fractions(
    volume_file: InputPathType,
    surface_file: InputPathType,
    accuracy: float,
    output_file: str,
    debug: bool = False,
    checkopts: bool = False,
    runner: Runner | None = None,
) -> MrisComputeVolumeFractionsOutputs:
    """
    Computes volume fractions based on a given surface and volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        volume_file: Input volume file.
        surface_file: Input surface file.
        accuracy: Required accuracy.
        output_file: Output volume file for the fractions.
        debug: Turn on debugging.
        checkopts: Don't run anything, just check options and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisComputeVolumeFractionsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_COMPUTE_VOLUME_FRACTIONS_METADATA)
    cargs = []
    cargs.append("mris_compute_volume_fractions")
    cargs.extend([
        "--vol",
        execution.input_file(volume_file)
    ])
    cargs.extend([
        "--surf",
        execution.input_file(surface_file)
    ])
    cargs.extend([
        "--acc",
        str(accuracy)
    ])
    cargs.extend([
        "--out",
        output_file
    ])
    if debug:
        cargs.append("--debug")
    if checkopts:
        cargs.append("--checkopts")
    ret = MrisComputeVolumeFractionsOutputs(
        root=execution.output_file("."),
        output_volume_file=execution.output_file(output_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_COMPUTE_VOLUME_FRACTIONS_METADATA",
    "MrisComputeVolumeFractionsOutputs",
    "mris_compute_volume_fractions",
]
