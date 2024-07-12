# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

AVSCALE_METADATA = Metadata(
    id="9434a53d1790fc0b88b3bbff7b8ba5a8b78ff929",
    name="avscale",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mydockerhubuser/avscale:latest",
)


class AvscaleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `avscale(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """The output file."""


def avscale(
    matrix_file: InputPathType,
    non_reference_volume: InputPathType | None = None,
    allparams_flag: bool = False,
    inverteddies_flag: bool = False,
    runner: Runner | None = None,
) -> AvscaleOutputs:
    """
    avscale by Unknown.
    
    A command line tool for computing affine transformations.
    
    Args:
        matrix_file: The path to the matrix file.
        non_reference_volume: The path to the non-reference volume.
        allparams_flag: Flag for all parameters.
        inverteddies_flag: Flag for inverted eddies.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AvscaleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(AVSCALE_METADATA)
    cargs = []
    cargs.append("avscale")
    if allparams_flag:
        cargs.append("--allparams")
    if inverteddies_flag:
        cargs.append("--inverteddies")
    cargs.append(execution.input_file(matrix_file))
    if non_reference_volume is not None:
        cargs.append(execution.input_file(non_reference_volume))
    cargs.append(">")
    cargs.append("output.txt")
    ret = AvscaleOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(f"output.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "AVSCALE_METADATA",
    "AvscaleOutputs",
    "avscale",
]
