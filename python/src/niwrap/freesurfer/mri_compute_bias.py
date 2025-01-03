# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_COMPUTE_BIAS_METADATA = Metadata(
    id="37471e0f282e684b7a904fea88a79fdbc35e80b4.boutiques",
    name="mri_compute_bias",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriComputeBiasOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_compute_bias(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """The output volume containing the bias correction result."""


def mri_compute_bias(
    subjects: list[str],
    output_volume: str,
    runner: Runner | None = None,
) -> MriComputeBiasOutputs:
    """
    Compute bias correction volumes for the given subjects and outputs the result to
    a specified volume.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjects: List of subjects for which bias correction is calculated.
        output_volume: Output volume where the result will be stored.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriComputeBiasOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_COMPUTE_BIAS_METADATA)
    cargs = []
    cargs.append("mri_compute_bias")
    cargs.extend(subjects)
    cargs.append(output_volume)
    ret = MriComputeBiasOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(output_volume),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_COMPUTE_BIAS_METADATA",
    "MriComputeBiasOutputs",
    "mri_compute_bias",
]
