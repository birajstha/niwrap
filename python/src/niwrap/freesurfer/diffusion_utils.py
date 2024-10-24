# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DIFFUSION_UTILS_METADATA = Metadata(
    id="644c1194ddc618947bb21fc39f90ede191a80b94.boutiques",
    name="diffusionUtils",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class DiffusionUtilsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `diffusion_utils(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def diffusion_utils(
    dummy_flag: bool = False,
    runner: Runner | None = None,
) -> DiffusionUtilsOutputs:
    """
    A utility related to diffusion data, potentially using the DIPY library.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        dummy_flag: Dummy input as no valid help information is provided due to\
            missing module.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DiffusionUtilsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DIFFUSION_UTILS_METADATA)
    cargs = []
    cargs.append("diffusionUtils")
    if dummy_flag:
        cargs.append("--dummy")
    ret = DiffusionUtilsOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DIFFUSION_UTILS_METADATA",
    "DiffusionUtilsOutputs",
    "diffusion_utils",
]
