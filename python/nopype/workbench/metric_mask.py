# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


METRIC_MASK_METADATA = Metadata(
    id="725ecb737ff1b37695fabc571f3688fba5cff65a",
    name="metric-mask",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class MetricMaskOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_mask(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric"""


def metric_mask(
    runner: Runner,
    metric: InputPathType,
    mask: InputPathType,
    metric_out: InputPathType,
    opt_column_column: str | None = None,
) -> MetricMaskOutputs:
    """
    MASK A METRIC FILE.
    
    By default, the output metric is a copy of the input metric, but with zeros
    wherever the mask metric is zero or negative. if -column is specified, the
    output contains only one column, the masked version of the specified input
    column.
    
    Args:
        runner: Command runner
        metric: the input metric
        mask: the mask metric
        metric_out: the output metric
        opt_column_column: select a single column: the column number or name
    Returns:
        NamedTuple of outputs (described in `MetricMaskOutputs`).
    """
    execution = runner.start_execution(METRIC_MASK_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metric-mask")
    cargs.append(execution.input_file(metric))
    cargs.append(execution.input_file(mask))
    cargs.append(execution.input_file(metric_out))
    if opt_column_column is not None:
        cargs.extend(["-column", opt_column_column])
    ret = MetricMaskOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(f"{pathlib.Path(metric_out).stem}"),
    )
    execution.run(cargs)
    return ret
