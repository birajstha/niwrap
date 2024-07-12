# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

METRIC_TFCE_METADATA = Metadata(
    id="e1784866bf0cf2e52a31a151d24f7764c43a1098",
    name="metric-tfce",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class MetricTfcePresmooth:
    """
    smooth the metric before running TFCE
    """
    kernel: float | int
    """the size of the gaussian smoothing kernel in mm, as sigma by default"""
    opt_fwhm: bool = False
    """kernel size is FWHM, not sigma"""
    
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
        cargs.append("-presmooth")
        cargs.append(str(self.kernel))
        if self.opt_fwhm:
            cargs.append("-fwhm")
        return cargs


@dataclasses.dataclass
class MetricTfceParameters:
    """
    set parameters for TFCE integral
    """
    e: float | int
    """exponent for cluster area (default 1.0)"""
    h: float | int
    """exponent for threshold value (default 2.0)"""
    
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
        cargs.append("-parameters")
        cargs.append(str(self.e))
        cargs.append(str(self.h))
        return cargs


class MetricTfceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_tfce(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric"""


def metric_tfce(
    surface: InputPathType,
    metric_in: InputPathType,
    metric_out: str,
    presmooth: MetricTfcePresmooth | None = None,
    opt_roi_roi_metric: InputPathType | None = None,
    parameters: MetricTfceParameters | None = None,
    opt_column_column: str | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
    runner: Runner | None = None,
) -> MetricTfceOutputs:
    """
    metric-tfce by Washington University School of Medicin.
    
    Do tfce on a metric file.
    
    This command does not do any statistical analysis. Please use something like
    PALM if you are just trying to do statistics on your data.
    
    Threshold-free cluster enhancement is a method to increase the relative
    value of regions that would form clusters in a standard thresholding test.
    This is accomplished by evaluating the integral of:
    
    e(h, p)^E * h^H * dh
    
    at each vertex p, where h ranges from 0 to the maximum value in the data,
    and e(h, p) is the extent of the cluster containing vertex p at threshold h.
    Negative values are similarly enhanced by negating the data, running the
    same process, and negating the result.
    
    When using -presmooth with -corrected-areas, note that it is an approximate
    correction within the smoothing algorithm (the TFCE correction is exact).
    Doing smoothing on individual surfaces before averaging/TFCE is preferred,
    when possible, in order to better tie the smoothing kernel size to the
    original feature size.
    
    The TFCE method is explained in: Smith SM, Nichols TE., "Threshold-free
    cluster enhancement: addressing problems of smoothing, threshold dependence
    and localisation in cluster inference." Neuroimage. 2009 Jan 1;44(1):83-98.
    PMID: 18501637.
    
    Args:
        surface: the surface to compute on.
        metric_in: the metric to run TFCE on.
        metric_out: the output metric.
        presmooth: smooth the metric before running TFCE.
        opt_roi_roi_metric: select a region of interest to run TFCE on: the\
            area to run TFCE on, as a metric.
        parameters: set parameters for TFCE integral.
        opt_column_column: select a single column: the column number or name.
        opt_corrected_areas_area_metric: vertex areas to use instead of\
            computing them from the surface: the corrected vertex areas, as a\
            metric.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MetricTfceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_TFCE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metric-tfce")
    cargs.append(execution.input_file(surface))
    cargs.append(execution.input_file(metric_in))
    cargs.append(metric_out)
    if presmooth is not None:
        cargs.extend(presmooth.run(execution))
    if opt_roi_roi_metric is not None:
        cargs.extend(["-roi", execution.input_file(opt_roi_roi_metric)])
    if parameters is not None:
        cargs.extend(parameters.run(execution))
    if opt_column_column is not None:
        cargs.extend(["-column", opt_column_column])
    if opt_corrected_areas_area_metric is not None:
        cargs.extend(["-corrected-areas", execution.input_file(opt_corrected_areas_area_metric)])
    ret = MetricTfceOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(f"{metric_out}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "METRIC_TFCE_METADATA",
    "MetricTfceOutputs",
    "MetricTfceParameters",
    "MetricTfcePresmooth",
    "metric_tfce",
]
