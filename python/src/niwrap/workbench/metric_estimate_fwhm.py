# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

METRIC_ESTIMATE_FWHM_METADATA = Metadata(
    id="0979a6909806aedc9eb064754b10178d219e3382",
    name="metric-estimate-fwhm",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class MetricEstimateFwhmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_estimate_fwhm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def metric_estimate_fwhm(
    surface: InputPathType,
    metric_in: InputPathType,
    opt_roi_roi_metric: InputPathType | None = None,
    opt_column_column: str | None = None,
    opt_whole_file: bool = False,
    opt_demean: bool = False,
    runner: Runner | None = None,
) -> MetricEstimateFwhmOutputs:
    """
    metric-estimate-fwhm by Washington University School of Medicin.
    
    Estimate fwhm smoothness of a metric file.
    
    Estimates the smoothness of the metric columns, printing the estimates to
    standard output. These estimates ignore variation in vertex spacing.
    
    Args:
        surface: the surface to use for distance and neighbor information.
        metric_in: the input metric.
        opt_roi_roi_metric: use only data within an ROI: the metric file to use\
            as an ROI.
        opt_column_column: select a single column to estimate smoothness of:\
            the column number or name.
        opt_whole_file: estimate for the whole file at once, not each column\
            separately.
        opt_demean: subtract the mean image before estimating smoothness.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MetricEstimateFwhmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_ESTIMATE_FWHM_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metric-estimate-fwhm")
    cargs.append(execution.input_file(surface))
    cargs.append(execution.input_file(metric_in))
    if opt_roi_roi_metric is not None:
        cargs.extend(["-roi", execution.input_file(opt_roi_roi_metric)])
    if opt_column_column is not None:
        cargs.extend(["-column", opt_column_column])
    if opt_whole_file:
        cargs.append("-whole-file")
    if opt_demean:
        cargs.append("-demean")
    ret = MetricEstimateFwhmOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "METRIC_ESTIMATE_FWHM_METADATA",
    "MetricEstimateFwhmOutputs",
    "metric_estimate_fwhm",
]
