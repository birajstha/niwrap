# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

METRIC_ERODE_METADATA = Metadata(
    id="4cf14a328dea03747fea8fba741b370398300e90.boutiques",
    name="metric-erode",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


class MetricErodeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_erode(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric"""


def metric_erode(
    metric: InputPathType,
    surface: InputPathType,
    distance: float,
    metric_out: str,
    opt_roi_roi_metric: InputPathType | None = None,
    opt_column_column: str | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
    runner: Runner | None = None,
) -> MetricErodeOutputs:
    """
    Erode a metric file.
    
    Around each vertex with a value of zero, set surrounding vertices to zero.
    The surrounding vertices are all immediate neighbors and all vertices within
    the specified distance.
    
    Note that the -corrected-areas option uses an approximate correction for
    distance along the surface.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        metric: the metric file to erode.
        surface: the surface to compute on.
        distance: distance in mm to erode.
        metric_out: the output metric.
        opt_roi_roi_metric: assume values outside this roi are nonzero: metric\
            file, positive values denote vertices that have data.
        opt_column_column: select a single column to erode: the column number\
            or name.
        opt_corrected_areas_area_metric: vertex areas to use instead of\
            computing them from the surface: the corrected vertex areas, as a\
            metric.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MetricErodeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_ERODE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metric-erode")
    cargs.append(execution.input_file(metric))
    cargs.append(execution.input_file(surface))
    cargs.append(str(distance))
    cargs.append(metric_out)
    if opt_roi_roi_metric is not None:
        cargs.extend([
            "-roi",
            execution.input_file(opt_roi_roi_metric)
        ])
    if opt_column_column is not None:
        cargs.extend([
            "-column",
            opt_column_column
        ])
    if opt_corrected_areas_area_metric is not None:
        cargs.extend([
            "-corrected-areas",
            execution.input_file(opt_corrected_areas_area_metric)
        ])
    ret = MetricErodeOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(metric_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "METRIC_ERODE_METADATA",
    "MetricErodeOutputs",
    "metric_erode",
]
