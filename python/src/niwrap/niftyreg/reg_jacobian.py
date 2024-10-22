# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

REG_JACOBIAN_METADATA = Metadata(
    id="235ec9ff93ed75c965eca2bf21da45d4db1dc09d.boutiques",
    name="reg_jacobian",
    package="niftyreg",
    container_image_tag="vnmd/niftyreg_1.4.0:20220819",
)


class RegJacobianOutputs(typing.NamedTuple):
    """
    Output object returned when calling `reg_jacobian(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_jacobian_file: OutputPathType
    """File containing the Jacobian determinant map"""
    output_jacobian_matrix_file: OutputPathType
    """File containing the Jacobian matrix map"""
    output_log_jacobian_file: OutputPathType
    """File containing the log of the Jacobian determinant map"""


def reg_jacobian(
    reference_image: InputPathType,
    runner: Runner | None = None,
) -> RegJacobianOutputs:
    """
    Tool to compute the Jacobian determinant map from a deformation field or control
    point lattice.
    
    Author: NiftyReg Developers
    
    URL: http://cmictig.cs.ucl.ac.uk/wiki/index.php/NiftyReg
    
    Args:
        reference_image: Filename of the reference image.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RegJacobianOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(REG_JACOBIAN_METADATA)
    cargs = []
    cargs.append("reg_jacobian")
    cargs.append("-ref")
    cargs.extend([
        "-target",
        execution.input_file(reference_image)
    ])
    cargs.append("[INPUT_TYPE]")
    cargs.append("[OUTPUT_OPTIONS]")
    cargs.append("[EXTRA_OPTIONS]")
    ret = RegJacobianOutputs(
        root=execution.output_file("."),
        output_jacobian_file=execution.output_file("[OUTPUT_JACOBIAN]"),
        output_jacobian_matrix_file=execution.output_file("[OUTPUT_JACOBIAN_MATRIX]"),
        output_log_jacobian_file=execution.output_file("[OUTPUT_LOG_JACOBIAN]"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "REG_JACOBIAN_METADATA",
    "RegJacobianOutputs",
    "reg_jacobian",
]
