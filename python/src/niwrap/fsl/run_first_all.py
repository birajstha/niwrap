# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

RUN_FIRST_ALL_METADATA = Metadata(
    id="969df88743cb206b767170e9a9d7af5b9fccc839.boutiques",
    name="run_first_all",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class RunFirstAllOutputs(typing.NamedTuple):
    """
    Output object returned when calling `run_first_all(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image_file: OutputPathType
    """Output image file"""


def run_first_all(
    input_image: InputPathType,
    output_image: str,
    method: typing.Literal["auto", "fast", "none"] | None = None,
    brainextract_flag: bool = False,
    structure: str | None = None,
    affine_matrix: InputPathType | None = None,
    threestage_flag: bool = False,
    debug_flag: bool = False,
    verbose_flag: bool = False,
    runner: Runner | None = None,
) -> RunFirstAllOutputs:
    """
    FIRST - FMRIB's Integrated Registration and Segmentation Tool for subcortical
    brain structures.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_image: Input image file.
        output_image: Output image file.
        method: Method for brain extraction (auto, fast, none or a numerical\
            threshold value).
        brainextract_flag: Input is already brain extracted.
        structure: Run only on one specified structure (e.g. L_Hipp) or a comma\
            separated list (no spaces).
        affine_matrix: Use affine matrix (do not re-run registration).
        threestage_flag: Use 3-stage affine registration (only currently for\
            hippocampus).
        debug_flag: Do not cleanup image output files (useful for debugging).
        verbose_flag: Verbose output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RunFirstAllOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RUN_FIRST_ALL_METADATA)
    cargs = []
    cargs.append("run_first_all")
    if method is not None:
        cargs.extend([
            "-m",
            method
        ])
    if brainextract_flag:
        cargs.append("-b")
    if structure is not None:
        cargs.extend([
            "-s",
            structure
        ])
    if affine_matrix is not None:
        cargs.extend([
            "-a",
            execution.input_file(affine_matrix)
        ])
    if threestage_flag:
        cargs.append("-3")
    if debug_flag:
        cargs.append("-d")
    if verbose_flag:
        cargs.append("-v")
    cargs.extend([
        "-i",
        execution.input_file(input_image)
    ])
    cargs.extend([
        "-o",
        output_image
    ])
    ret = RunFirstAllOutputs(
        root=execution.output_file("."),
        output_image_file=execution.output_file(output_image),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "RUN_FIRST_ALL_METADATA",
    "RunFirstAllOutputs",
    "run_first_all",
]
