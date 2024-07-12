# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SURFACE_COORDINATES_TO_METRIC_METADATA = Metadata(
    id="6682b45237215db3a76cf1df816c535acdd189bf",
    name="surface-coordinates-to-metric",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class SurfaceCoordinatesToMetricOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_coordinates_to_metric(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric"""


def surface_coordinates_to_metric(
    surface: InputPathType,
    metric_out: str,
    runner: Runner | None = None,
) -> SurfaceCoordinatesToMetricOutputs:
    """
    surface-coordinates-to-metric by Washington University School of Medicin.
    
    Make metric file of surface coordinates.
    
    Puts the coordinates of the surface into a 3-map metric file, as x, y, z.
    
    Args:
        surface: the surface to use the coordinates of.
        metric_out: the output metric.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceCoordinatesToMetricOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_COORDINATES_TO_METRIC_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-coordinates-to-metric")
    cargs.append(execution.input_file(surface))
    cargs.append(metric_out)
    ret = SurfaceCoordinatesToMetricOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(f"{metric_out}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_COORDINATES_TO_METRIC_METADATA",
    "SurfaceCoordinatesToMetricOutputs",
    "surface_coordinates_to_metric",
]
