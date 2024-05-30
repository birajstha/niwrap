# This file was auto generated by Styx.
# Do not edit this file directly.

import pathlib
import typing

from styxdefs import *


METRIC_FILL_HOLES_METADATA = Metadata(
    id="e8f36c2a2a1abd0a92c85dce38eca355263bf9dc",
    name="metric-fill-holes",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class MetricFillHolesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metric_fill_holes(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output ROI metric"""


def metric_fill_holes(
    surface: InputPathType,
    metric_in: InputPathType,
    metric_out: InputPathType,
    opt_corrected_areas_area_metric: InputPathType | None = None,
    runner: Runner = None,
) -> MetricFillHolesOutputs:
    """
    metric-fill-holes by Washington University School of Medicin.
    
    Fill holes in an roi metric.
    
    Finds all connected areas that are not included in the ROI, and writes ones
    into all but the largest one, in terms of surface area.
    
    Args:
        surface: the surface to use for neighbor information
        metric_in: the input ROI metric
        metric_out: the output ROI metric
        opt_corrected_areas_area_metric: vertex areas to use instead of
            computing them from the surface: the corrected vertex areas, as a metric
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `MetricFillHolesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METRIC_FILL_HOLES_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metric-fill-holes")
    cargs.append(execution.input_file(surface))
    cargs.append(execution.input_file(metric_in))
    cargs.append(execution.input_file(metric_out))
    if opt_corrected_areas_area_metric is not None:
        cargs.extend(["-corrected-areas", execution.input_file(opt_corrected_areas_area_metric)])
    ret = MetricFillHolesOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(f"{pathlib.Path(metric_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "METRIC_FILL_HOLES_METADATA",
    "MetricFillHolesOutputs",
    "metric_fill_holes",
]
