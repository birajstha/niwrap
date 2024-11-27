# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_TRANSFORM_METADATA = Metadata(
    id="bc7a45fd27e432a438c7967d047a12047b926e4c.boutiques",
    name="mri_transform",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriTransformOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_transform(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    transformed_output: OutputPathType
    """Transformed output volume"""


def mri_transform(
    input_volume: InputPathType,
    lta_file: InputPathType,
    output_file: str,
    out_like: InputPathType | None = None,
    invert: bool = False,
    runner: Runner | None = None,
) -> MriTransformOutputs:
    """
    Applies a linear transform to an MRI volume and writes out the result.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input MRI volume.
        lta_file: Linear Transform Array (LTA) file.
        output_file: Output file for the transformed MRI volume.
        out_like: Set output volume parameters like the reference volume.
        invert: Invert transform coordinates.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriTransformOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_TRANSFORM_METADATA)
    cargs = []
    cargs.append("mri_transform")
    cargs.append(execution.input_file(input_volume))
    cargs.append(execution.input_file(lta_file))
    cargs.append(output_file)
    if out_like is not None:
        cargs.extend([
            "-out_like",
            execution.input_file(out_like)
        ])
    if invert:
        cargs.append("-I")
    ret = MriTransformOutputs(
        root=execution.output_file("."),
        transformed_output=execution.output_file(output_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_TRANSFORM_METADATA",
    "MriTransformOutputs",
    "mri_transform",
]
