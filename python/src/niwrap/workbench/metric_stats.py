# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

METRIC_STATS_METADATA = Metadata(
    id="b976276141b96f41a553181c132766ea053d2cf5",
    name="metric-stats",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class MetricStatsRoi:
    """
    only consider data inside an roi
    """
    opt_match_maps: bool = False
    """each column of input uses the corresponding column from the roi file"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        if self.opt_match_maps:
            cargs.append("-match-maps")
        return cargs


class MetricStatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_stats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def metric_stats(
    metric_in: InputPathType,
    opt_reduce_operation: str | None = None,
    opt_percentile_percent: float | int | None = None,
    opt_column_column: str | None = None,
    roi: MetricStatsRoi | None = None,
    opt_show_map_name: bool = False,
    runner: Runner = None,
) -> MetricStatsOutputs:
    """
    metric-stats by Washington University School of Medicin.
    
    Spatial statistics on a metric file.
    
    For each column of the input, a line of text is printed, resulting from the
    specified reduction or percentile operation. Use -column to only give output
    for a single column. If the -roi option is used without -match-maps, then
    each line will contain as many numbers as there are maps in the ROI file,
    separated by tab characters. Exactly one of -reduce or -percentile must be
    specified.
    
    The argument to the -reduce option must be one of the following:
    
    MAX: the maximum value
    MIN: the minimum value
    INDEXMAX: the 1-based index of the maximum value
    INDEXMIN: the 1-based index of the minimum value
    SUM: add all values
    PRODUCT: multiply all values
    MEAN: the mean of the data
    STDEV: the standard deviation (N denominator)
    SAMPSTDEV: the sample standard deviation (N-1 denominator)
    VARIANCE: the variance of the data
    TSNR: mean divided by sample standard deviation (N-1 denominator)
    COV: sample standard deviation (N-1 denominator) divided by mean
    L2NORM: square root of sum of squares
    MEDIAN: the median of the data
    MODE: the mode of the data
    COUNT_NONZERO: the number of nonzero elements in the data
    .
    
    Args:
        metric_in: the input metric.
        opt_reduce_operation: use a reduction operation: the reduction\
            operation.
        opt_percentile_percent: give the value at a percentile: the percentile\
            to find, must be between 0 and 100.
        opt_column_column: only display output for one column: the column\
            number or name.
        roi: only consider data inside an roi.
        opt_show_map_name: print map index and name before each output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MetricStatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_STATS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metric-stats")
    cargs.append(execution.input_file(metric_in))
    if opt_reduce_operation is not None:
        cargs.extend(["-reduce", opt_reduce_operation])
    if opt_percentile_percent is not None:
        cargs.extend(["-percentile", str(opt_percentile_percent)])
    if opt_column_column is not None:
        cargs.extend(["-column", opt_column_column])
    if roi is not None:
        cargs.extend(["-roi", *roi.run(execution)])
    if opt_show_map_name:
        cargs.append("-show-map-name")
    ret = MetricStatsOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "METRIC_STATS_METADATA",
    "MetricStatsOutputs",
    "MetricStatsRoi",
    "metric_stats",
]
