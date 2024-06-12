# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

CIFTI_STATS_METADATA = Metadata(
    id="040f30e34270fbea27c196902bba1d25b9b6b247",
    name="cifti-stats",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class CiftiStatsRoi:
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


class CiftiStatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_stats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def cifti_stats(
    cifti_in: InputPathType,
    opt_reduce_operation: str | None = None,
    opt_percentile_percent: float | int | None = None,
    opt_column_column: int | None = None,
    roi: CiftiStatsRoi | None = None,
    opt_show_map_name: bool = False,
    runner: Runner = None,
) -> CiftiStatsOutputs:
    """
    cifti-stats by Washington University School of Medicin.
    
    Statistics along cifti columns.
    
    For each column of the input, a line of text is printed, resulting from the
    specified reduction or percentile operation. If -roi is specified without
    -match-maps, then each line will contain as many numbers as there are maps
    in the ROI file, separated by tab characters. Use -column to only give
    output for a single data column. Exactly one of -reduce or -percentile must
    be specified.
    
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
        cifti_in: the input cifti.
        opt_reduce_operation: use a reduction operation: the reduction\
            operation.
        opt_percentile_percent: give the value at a percentile: the percentile\
            to find, must be between 0 and 100.
        opt_column_column: only display output for one column: the column index\
            (starting from 1).
        roi: only consider data inside an roi.
        opt_show_map_name: print column index and name before each output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiStatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_STATS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-stats")
    cargs.append(execution.input_file(cifti_in))
    if opt_reduce_operation is not None:
        cargs.extend(["-reduce", opt_reduce_operation])
    if opt_percentile_percent is not None:
        cargs.extend(["-percentile", str(opt_percentile_percent)])
    if opt_column_column is not None:
        cargs.extend(["-column", str(opt_column_column)])
    if roi is not None:
        cargs.extend(["-roi", *roi.run(execution)])
    if opt_show_map_name:
        cargs.append("-show-map-name")
    ret = CiftiStatsOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_STATS_METADATA",
    "CiftiStatsOutputs",
    "CiftiStatsRoi",
    "cifti_stats",
]
