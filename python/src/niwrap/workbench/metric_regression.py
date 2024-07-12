# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

METRIC_REGRESSION_METADATA = Metadata(
    id="3b3de7392bf787c7bd1caf141158a3b9fb08fc1d",
    name="metric-regression",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class MetricRegressionRemove:
    """
    specify a metric to regress out
    """
    metric: InputPathType
    """the metric file to use"""
    opt_remove_column_column: str | None = None
    """select a column to use, rather than all: the column number or name"""
    
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
        cargs.append("-remove")
        cargs.append(execution.input_file(self.metric))
        if self.opt_remove_column_column is not None:
            cargs.extend(["-remove-column", self.opt_remove_column_column])
        return cargs


@dataclasses.dataclass
class MetricRegressionKeep:
    """
    specify a metric to include in regression, but not remove
    """
    metric: InputPathType
    """the metric file to use"""
    opt_keep_column_column: str | None = None
    """select a column to use, rather than all: the column number or name"""
    
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
        cargs.append("-keep")
        cargs.append(execution.input_file(self.metric))
        if self.opt_keep_column_column is not None:
            cargs.extend(["-keep-column", self.opt_keep_column_column])
        return cargs


class MetricRegressionOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_regression(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric"""


def metric_regression(
    metric_in: InputPathType,
    metric_out: str,
    opt_roi_roi_metric: InputPathType | None = None,
    opt_column_column: str | None = None,
    remove: list[MetricRegressionRemove] | None = None,
    keep: list[MetricRegressionKeep] | None = None,
    runner: Runner | None = None,
) -> MetricRegressionOutputs:
    """
    metric-regression by Washington University School of Medicin.
    
    Regress spatial map out of a metric file.
    
    For each regressor, its mean across the surface is subtracted from its data.
    Each input map is then regressed against these, and a constant term. The
    resulting regressed slopes of all regressors specified with -remove are
    multiplied with their respective regressor maps, and these are subtracted
    from the input map.
    
    Args:
        metric_in: the metric to regress from.
        metric_out: the output metric.
        opt_roi_roi_metric: only regress inside an roi: the area to use for\
            regression, as a metric.
        opt_column_column: select a single column to regress from: the column\
            number or name.
        remove: specify a metric to regress out.
        keep: specify a metric to include in regression, but not remove.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MetricRegressionOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_REGRESSION_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metric-regression")
    cargs.append(execution.input_file(metric_in))
    cargs.append(metric_out)
    if opt_roi_roi_metric is not None:
        cargs.extend(["-roi", execution.input_file(opt_roi_roi_metric)])
    if opt_column_column is not None:
        cargs.extend(["-column", opt_column_column])
    if remove is not None:
        cargs.extend([a for c in [s.run(execution) for s in remove] for a in c])
    if keep is not None:
        cargs.extend([a for c in [s.run(execution) for s in keep] for a in c])
    ret = MetricRegressionOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(f"{metric_out}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "METRIC_REGRESSION_METADATA",
    "MetricRegressionKeep",
    "MetricRegressionOutputs",
    "MetricRegressionRemove",
    "metric_regression",
]
