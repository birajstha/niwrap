# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

NEURO_DECONVOLVE_PY_METADATA = Metadata(
    id="7deab2368a36fa0ebe35904371306494cb49280c.boutiques",
    name="neuro_deconvolve.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class NeuroDeconvolvePyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `neuro_deconvolve_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_head: OutputPathType
    """Main default output head file"""
    output_brik: OutputPathType
    """Main default output BRIK file"""
    kernel_file_out: OutputPathType | None
    """File storing the response kernel"""


def neuro_deconvolve_py(
    input_file: InputPathType,
    prefix: str,
    script: str,
    kernel: str | None = None,
    kernel_file: str | None = None,
    mask_dset: InputPathType | None = None,
    old_style: bool = False,
    tr: float | None = None,
    tr_nup: float | None = None,
    verbosity: float | None = None,
    runner: Runner | None = None,
) -> NeuroDeconvolvePyOutputs:
    """
    Generate a script to apply 3dTfitter to deconvolve an MRI signal (BOLD response
    curve) into a neuro response curve.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_file: Set the data to deconvolve.
        prefix: Set the prefix for output filenames.
        script: Specify the name of the output script.
        kernel: Set the response kernel.
        kernel_file: Set the filename to store the kernel in; should be at the\
            upsampled TR.
        mask_dset: Set a mask dataset for 3dTfitter to use.
        old_style: Make old-style script (pre-2015.02.24) for 1D case.
        tr: Set the scanner TR; needed for 1D formatted input files.
        tr_nup: Upsample factor for TR; number of pieces each original TR is\
            divided into.
        verbosity: Set the verbose level.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `NeuroDeconvolvePyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(NEURO_DECONVOLVE_PY_METADATA)
    cargs = []
    cargs.append("neuro_deconvolve.py")
    cargs.append(execution.input_file(input_file))
    cargs.append(prefix)
    cargs.append(script)
    if kernel is not None:
        cargs.extend([
            "-kernel",
            kernel
        ])
    if kernel_file is not None:
        cargs.extend([
            "-kernel_file",
            kernel_file
        ])
    if mask_dset is not None:
        cargs.extend([
            "-mask_dset",
            execution.input_file(mask_dset)
        ])
    if old_style:
        cargs.append("-old")
    if tr is not None:
        cargs.extend([
            "-tr",
            str(tr)
        ])
    if tr_nup is not None:
        cargs.extend([
            "-tr_nup",
            str(tr_nup)
        ])
    if verbosity is not None:
        cargs.extend([
            "-verb",
            str(verbosity)
        ])
    ret = NeuroDeconvolvePyOutputs(
        root=execution.output_file("."),
        output_head=execution.output_file(prefix + "+orig.HEAD"),
        output_brik=execution.output_file(prefix + "+orig.BRIK"),
        kernel_file_out=execution.output_file(kernel_file) if (kernel_file is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "NEURO_DECONVOLVE_PY_METADATA",
    "NeuroDeconvolvePyOutputs",
    "neuro_deconvolve_py",
]
