# This file was auto generated by Styx.
# Do not edit this file directly.

import pathlib
import typing

from styxdefs import *


METRIC_VECTOR_OPERATION_METADATA = Metadata(
    id="27bde668dd4a07828ba62ded018123819a06bde1",
    name="metric-vector-operation",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class MetricVectorOperationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_vector_operation(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output file"""


def metric_vector_operation(
    vectors_a: InputPathType,
    vectors_b: InputPathType,
    operation: str,
    metric_out: InputPathType,
    opt_normalize_a: bool = False,
    opt_normalize_b: bool = False,
    opt_normalize_output: bool = False,
    opt_magnitude: bool = False,
    runner: Runner = None,
) -> MetricVectorOperationOutputs:
    """
    metric-vector-operation by Washington University School of Medicin.
    
    Do a vector operation on metric files.
    
    Does a vector operation on two metric files (that must have a multiple of 3
    columns). Either of the inputs may have multiple vectors (more than 3
    columns), but not both (at least one must have exactly 3 columns). The
    -magnitude and -normalize-output options may not be specified together, or
    with an operation that returns a scalar (dot product). The <operation>
    parameter must be one of the following:
    
    DOT
    CROSS
    ADD
    SUBTRACT.
    
    Args:
        vectors_a: first vector input file
        vectors_b: second vector input file
        operation: what vector operation to do
        metric_out: the output file
        opt_normalize_a: normalize vectors of first input
        opt_normalize_b: normalize vectors of second input
        opt_normalize_output: normalize output vectors (not valid for dot
            product)
        opt_magnitude: output the magnitude of the result (not valid for dot
            product)
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `MetricVectorOperationOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_VECTOR_OPERATION_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metric-vector-operation")
    cargs.append(execution.input_file(vectors_a))
    cargs.append(execution.input_file(vectors_b))
    cargs.append(operation)
    cargs.append(execution.input_file(metric_out))
    if opt_normalize_a:
        cargs.append("-normalize-a")
    if opt_normalize_b:
        cargs.append("-normalize-b")
    if opt_normalize_output:
        cargs.append("-normalize-output")
    if opt_magnitude:
        cargs.append("-magnitude")
    ret = MetricVectorOperationOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(f"{pathlib.Path(metric_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "METRIC_VECTOR_OPERATION_METADATA",
    "MetricVectorOperationOutputs",
    "metric_vector_operation",
]
