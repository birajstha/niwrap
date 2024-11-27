# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SIGLOSS_METADATA = Metadata(
    id="925adf9e97058d87551f4f3a27c9b5b1c1c21397.boutiques",
    name="sigloss",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class SiglossOutputs(typing.NamedTuple):
    """
    Output object returned when calling `sigloss(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def sigloss(
    input_b0map: InputPathType,
    output_sigloss: str,
    input_mask: InputPathType | None = None,
    echo_time: float | None = None,
    slice_direction: typing.Literal["x", "y", "z"] | None = None,
    verbose_flag: bool = False,
    runner: Runner | None = None,
) -> SiglossOutputs:
    """
    Estimates signal loss from a field map (in rad/s).
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_b0map: Input b0 map image filename (in rad/s).
        output_sigloss: Output signal loss image filename.
        input_mask: Input mask filename.
        echo_time: Echo time (in seconds).
        slice_direction: Slice direction (either x, y or z).
        verbose_flag: Switch on diagnostic messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SiglossOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SIGLOSS_METADATA)
    cargs = []
    cargs.append("sigloss")
    cargs.extend([
        "-i",
        execution.input_file(input_b0map)
    ])
    cargs.extend([
        "-s",
        output_sigloss
    ])
    if input_mask is not None:
        cargs.extend([
            "-m",
            execution.input_file(input_mask)
        ])
    if echo_time is not None:
        cargs.extend([
            "--te",
            str(echo_time)
        ])
    if slice_direction is not None:
        cargs.extend([
            "-d",
            slice_direction
        ])
    if verbose_flag:
        cargs.append("-v")
    ret = SiglossOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SIGLOSS_METADATA",
    "SiglossOutputs",
    "sigloss",
]
