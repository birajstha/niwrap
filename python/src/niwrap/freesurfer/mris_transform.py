# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_TRANSFORM_METADATA = Metadata(
    id="8c13e0715d0d51bf0467c4fca8ecf1a12c72c46b.boutiques",
    name="mris_transform",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisTransformOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_transform(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    transformed_output_surface: OutputPathType
    """Transformed output surface file."""


def mris_transform(
    input_surface: InputPathType,
    transform: InputPathType,
    output_surface: str,
    trx_src: InputPathType | None = None,
    trx_dst: InputPathType | None = None,
    is_inverse: bool = False,
    runner: Runner | None = None,
) -> MrisTransformOutputs:
    """
    A tool to transform surfaces from one space to another using image transforms.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_surface: Input surface file, e.g., lh.pial.
        transform: Image-to-image transform file, e.g., LTA or M3Z.
        output_surface: Output surface file, e.g., lh.out.pial.
        trx_src: Specify the source geometry if the transform was created by\
            MNI/mritotal or FSL/flirt.
        trx_dst: Specify the destination geometry if the transform does not\
            include this information or the path in the M3Z is invalid.
        is_inverse: Use this option when using a transform from destination to\
            source space.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisTransformOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_TRANSFORM_METADATA)
    cargs = []
    cargs.append("mris_transform")
    cargs.append(execution.input_file(input_surface))
    cargs.append(execution.input_file(transform))
    cargs.append(output_surface)
    if trx_src is not None:
        cargs.extend([
            "--trx-src",
            execution.input_file(trx_src)
        ])
    if trx_dst is not None:
        cargs.extend([
            "--trx-dst",
            execution.input_file(trx_dst)
        ])
    if is_inverse:
        cargs.append("--is-inverse")
    ret = MrisTransformOutputs(
        root=execution.output_file("."),
        transformed_output_surface=execution.output_file(output_surface),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_TRANSFORM_METADATA",
    "MrisTransformOutputs",
    "mris_transform",
]