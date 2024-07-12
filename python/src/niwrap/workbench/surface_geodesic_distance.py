# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SURFACE_GEODESIC_DISTANCE_METADATA = Metadata(
    id="b60647202511b479374ed48c2e22f1fe35908450",
    name="surface-geodesic-distance",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class SurfaceGeodesicDistanceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_geodesic_distance(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric"""


def surface_geodesic_distance(
    surface: InputPathType,
    vertex: int,
    metric_out: str,
    opt_naive: bool = False,
    opt_limit_limit_mm: float | int | None = None,
    opt_corrected_areas_area_metric: InputPathType | None = None,
    runner: Runner | None = None,
) -> SurfaceGeodesicDistanceOutputs:
    """
    surface-geodesic-distance by Washington University School of Medicin.
    
    Compute geodesic distance from one vertex to the entire surface.
    
    Unless -limit is specified, computes the geodesic distance from the
    specified vertex to all others. The result is output as a single column
    metric file, with a value of -1 for vertices that the distance was not
    computed for.
    
    The -corrected-areas option should be used when the input is a group average
    surface - group average surfaces have significantly less surface area than
    individual surfaces do, and therefore distances measured on them would be
    smaller than measuring them on individual surfaces. In this case, the input
    to this option should be a group average of the output of
    -surface-vertex-areas for each subject.
    
    If -naive is not specified, the algorithm uses not just immediate neighbors,
    but also neighbors derived from crawling across pairs of triangles that
    share an edge.
    
    Args:
        surface: the surface to compute on.
        vertex: the vertex to compute geodesic distance from.
        metric_out: the output metric.
        opt_naive: use only neighbors, don't crawl triangles (not recommended).
        opt_limit_limit_mm: stop at a certain distance: distance in mm to stop\
            at.
        opt_corrected_areas_area_metric: vertex areas to use instead of\
            computing them from the surface: the corrected vertex areas, as a\
            metric.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceGeodesicDistanceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_GEODESIC_DISTANCE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-geodesic-distance")
    cargs.append(execution.input_file(surface))
    cargs.append(str(vertex))
    cargs.append(metric_out)
    if opt_naive:
        cargs.append("-naive")
    if opt_limit_limit_mm is not None:
        cargs.extend(["-limit", str(opt_limit_limit_mm)])
    if opt_corrected_areas_area_metric is not None:
        cargs.extend(["-corrected-areas", execution.input_file(opt_corrected_areas_area_metric)])
    ret = SurfaceGeodesicDistanceOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(f"{metric_out}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_GEODESIC_DISTANCE_METADATA",
    "SurfaceGeodesicDistanceOutputs",
    "surface_geodesic_distance",
]
