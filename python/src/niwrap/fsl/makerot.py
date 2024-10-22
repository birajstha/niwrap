# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MAKEROT_METADATA = Metadata(
    id="50a219082fe22aa0bb97ef18740853d5f81b69d7.boutiques",
    name="makerot",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class MakerotOutputs(typing.NamedTuple):
    """
    Output object returned when calling `makerot(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    matrix_output: OutputPathType | None
    """Output file for the rotation matrix"""


def makerot(
    theta: float,
    axis: str | None = None,
    cov: InputPathType | None = None,
    center: str | None = None,
    output_file: InputPathType | None = None,
    verbose_flag: bool = False,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> MakerotOutputs:
    """
    Tool to create a rotation matrix for a given angle and axis of rotation.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        theta: Angle of rotation (in degrees).
        axis: Unnormalized axis vector (comma separated).
        cov: Image filename used for center of volume.
        center: Center of rotation in mm (comma separated).
        output_file: Output filename for matrix.
        verbose_flag: Switch on diagnostic messages.
        help_flag: Display help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MakerotOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MAKEROT_METADATA)
    cargs = []
    cargs.append("makerot")
    if axis is not None:
        cargs.extend([
            "--axis",
            axis
        ])
    if cov is not None:
        cargs.extend([
            "--cov",
            execution.input_file(cov)
        ])
    if center is not None:
        cargs.extend([
            "--centre",
            center
        ])
    if output_file is not None:
        cargs.extend([
            "--out",
            execution.input_file(output_file)
        ])
    if verbose_flag:
        cargs.append("--verbose")
    if help_flag:
        cargs.append("--help")
    cargs.extend([
        "--theta",
        str(theta)
    ])
    ret = MakerotOutputs(
        root=execution.output_file("."),
        matrix_output=execution.output_file(pathlib.Path(output_file).name) if (output_file is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MAKEROT_METADATA",
    "MakerotOutputs",
    "makerot",
]
