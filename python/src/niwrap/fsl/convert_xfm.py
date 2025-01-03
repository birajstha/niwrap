# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CONVERT_XFM_METADATA = Metadata(
    id="b079bee0db4c9532ed2211cab0dd571d7a59ebde.boutiques",
    name="convert_xfm",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class ConvertXfmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `convert_xfm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_trasnformation: OutputPathType | None
    """Output transformation matrix."""


def convert_xfm(
    in_file: InputPathType,
    out_file: str | None = None,
    invert_xfm: bool = False,
    concat_xfm: InputPathType | None = None,
    fix_scale_skew: InputPathType | None = None,
    runner: Runner | None = None,
) -> ConvertXfmOutputs:
    """
    convert_xfm is a utility that is used to convert between different
    transformation file formats. It can read and write ascii 4x4 matrices. In
    addition, it can be used to concatenate two transforms (using -concat with the
    second transform) or to find the inverse transformation (using -inverse).
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        in_file: Input transformation matrix.
        out_file: Final transformation matrix.
        invert_xfm: Invert input transformation.
        concat_xfm: A File. Write joint transformation of two input matrices.
        fix_scale_skew: A File. Use secondary matrix to fix scale and skew.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ConvertXfmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONVERT_XFM_METADATA)
    cargs = []
    cargs.append("convert_xfm")
    if out_file is not None:
        cargs.extend([
            "-omat",
            out_file
        ])
    if invert_xfm:
        cargs.append("-inverse")
    if concat_xfm is not None:
        cargs.extend([
            "-concat",
            execution.input_file(concat_xfm)
        ])
    if fix_scale_skew is not None:
        cargs.extend([
            "-fixscaleskew",
            execution.input_file(fix_scale_skew)
        ])
    cargs.append(execution.input_file(in_file))
    ret = ConvertXfmOutputs(
        root=execution.output_file("."),
        output_trasnformation=execution.output_file(out_file) if (out_file is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CONVERT_XFM_METADATA",
    "ConvertXfmOutputs",
    "convert_xfm",
]
