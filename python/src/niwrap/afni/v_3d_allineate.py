# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_ALLINEATE_METADATA = Metadata(
    id="9e9b34eca4cf79e9ab56b274a89a3cd8dc932bed.boutiques",
    name="3dAllineate",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dAllineateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_allineate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_brik: OutputPathType
    """Output dataset brick file"""
    out_head: OutputPathType
    """Output dataset head file"""
    out_param_save: OutputPathType | None
    """File holding saved warp parameters"""
    out_matrix_save: OutputPathType | None
    """File holding saved matrix transformations"""


def v_3d_allineate(
    source: InputPathType,
    prefix: str,
    base: InputPathType | None = None,
    param_save: str | None = None,
    param_apply: str | None = None,
    matrix_save: str | None = None,
    matrix_apply: str | None = None,
    cost: str | None = None,
    interp: str | None = None,
    final: str | None = None,
    nmatch: float | None = None,
    nopad: bool = False,
    verbose: bool = False,
    quiet: bool = False,
    runner: Runner | None = None,
) -> V3dAllineateOutputs:
    """
    Program to align one dataset (the 'source') to a 'base' dataset using an affine
    (matrix) transformation of space.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        source: Source dataset file.
        prefix: Output prefix.
        base: Base dataset file.
        param_save: Save the warp parameters in ASCII (.1D) format into file.
        param_apply: Read warp parameters from file and apply them to the\
            source dataset.
        matrix_save: Save the transformation matrix for each sub-brick into\
            file.
        matrix_apply: Use the matrices in file to define the spatial\
            transformations to be applied.
        cost: Defines the 'cost' function that defines the matching between the\
            source and the base.
        interp: Defines interpolation method to use during matching process.
        final: Defines the interpolation mode used to create the output dataset.
        nmatch: Use at most 'nnn' scattered points to match the datasets.
        nopad: Do not use zero-padding on the base image.
        verbose: Print out verbose progress reports.
        quiet: Don't print out verbose stuff.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dAllineateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_ALLINEATE_METADATA)
    cargs = []
    cargs.append("3dAllineate")
    cargs.append(execution.input_file(source))
    if base is not None:
        cargs.extend([
            "-base",
            execution.input_file(base)
        ])
    cargs.extend([
        "-prefix",
        prefix
    ])
    if param_save is not None:
        cargs.extend([
            "-1Dparam_save",
            param_save
        ])
    if param_apply is not None:
        cargs.extend([
            "-1Dparam_apply",
            param_apply
        ])
    if matrix_save is not None:
        cargs.extend([
            "-1Dmatrix_save",
            matrix_save
        ])
    if matrix_apply is not None:
        cargs.extend([
            "-1Dmatrix_apply",
            matrix_apply
        ])
    if cost is not None:
        cargs.extend([
            "-cost",
            cost
        ])
    if interp is not None:
        cargs.extend([
            "-interp",
            interp
        ])
    if final is not None:
        cargs.extend([
            "-final",
            final
        ])
    if nmatch is not None:
        cargs.extend([
            "-nmatch",
            str(nmatch)
        ])
    if nopad:
        cargs.append("-nopad")
    if verbose:
        cargs.append("-verb")
    if quiet:
        cargs.append("-quiet")
    ret = V3dAllineateOutputs(
        root=execution.output_file("."),
        out_brik=execution.output_file(prefix + "+orig.BRIK"),
        out_head=execution.output_file(prefix + "+orig.HEAD"),
        out_param_save=execution.output_file(param_save) if (param_save is not None) else None,
        out_matrix_save=execution.output_file(matrix_save) if (matrix_save is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dAllineateOutputs",
    "V_3D_ALLINEATE_METADATA",
    "v_3d_allineate",
]
