# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

QDELAUNAY_METADATA = Metadata(
    id="6ffd24be5e49d65ad58c48581dbc1c38e779c71c.boutiques",
    name="qdelaunay",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class QdelaunayOutputs(typing.NamedTuple):
    """
    Output object returned when calling `qdelaunay(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def qdelaunay(
    input_file: InputPathType,
    furthest_site: bool = False,
    triangulated_output: bool = False,
    joggled_input: bool = False,
    joggle_range: float | None = None,
    search_simplex: bool = False,
    point_infinity: bool = False,
    delaunay_visible: str | None = None,
    delaunay_regions: str | None = None,
    trace_level: float | None = None,
    check: bool = False,
    statistics_: bool = False,
    verify: bool = False,
    output_stdout: bool = False,
    facets_summary: float | None = None,
    input_file_option: InputPathType | None = None,
    output_file_option: InputPathType | None = None,
    trace_point: float | None = None,
    trace_merge: float | None = None,
    trace_merge_width: float | None = None,
    stop_point: float | None = None,
    stop_cone_point: float | None = None,
    centrum_radius: float | None = None,
    max_angle_cosine: float | None = None,
    perturb_factor: float | None = None,
    min_facet_width: float | None = None,
    facet_dump: bool = False,
    geomview: bool = False,
    vertices_incident: bool = False,
    mathematica: bool = False,
    off_format: bool = False,
    point_coordinates: bool = False,
    summary: bool = False,
    runner: Runner | None = None,
) -> QdelaunayOutputs:
    """
    Compute the Delaunay triangulation using Qhull.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_file: Input file containing point coordinates.
        furthest_site: Compute furthest-site Delaunay triangulation.
        triangulated_output: Triangulated output.
        joggled_input: Joggled input instead of merged facets.
        joggle_range: Randomly joggle input in range [-n,n].
        search_simplex: Search all points for the initial simplex.
        point_infinity: Add point-at-infinity to Delaunay triangulation.
        delaunay_visible: Print Delaunay region if visible from point n, -n if\
            not.
        delaunay_regions: Print Delaunay regions that include point n, -n if\
            not.
        trace_level: Trace at level n, 4=all, 5=mem/gauss, -1= events.
        check: Check frequently during execution.
        statistics_: Print statistics.
        verify: Verify result: structure, convexity, and in-circle test.
        output_stdout: Send all output to stdout.
        facets_summary: Report summary when n or more facets created.
        input_file_option: Input data from file, no spaces or single quotes.
        output_file_option: Output results to file, may be enclosed in single\
            quotes.
        trace_point: Turn on tracing when point n added to hull.
        trace_merge: Turn on tracing at merge n.
        trace_merge_width: Trace merge facets when width > n.
        stop_point: Stop Qhull after adding point n, -n for before.
        stop_cone_point: Stop Qhull after building cone for point n.
        centrum_radius: Radius of centrum (roundoff added). Merge facets if\
            non-convex.
        max_angle_cosine: Cosine of maximum angle. Merge facets if cosine > n\
            or non-convex.
        perturb_factor: Randomly perturb computations by a factor of [1-n,1+n].
        min_facet_width: Min facet width for outside point (before roundoff).
        facet_dump: Facet dump.
        geomview: Geomview output.
        vertices_incident: Vertices incident to each Delaunay region.
        mathematica: Mathematica output (2-d only, lifted to a paraboloid).
        off_format: OFF format (dim, points, and facets as a paraboloid).
        point_coordinates: Point coordinates (lifted to a paraboloid).
        summary: Summary (stderr).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `QdelaunayOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(QDELAUNAY_METADATA)
    cargs = []
    cargs.append("qdelaunay")
    cargs.append(execution.input_file(input_file))
    if furthest_site:
        cargs.append("Qu")
    if triangulated_output:
        cargs.append("Qt")
    if joggled_input:
        cargs.append("QJ")
    if joggle_range is not None:
        cargs.extend([
            "QJn",
            str(joggle_range)
        ])
    if search_simplex:
        cargs.append("Qs")
    if point_infinity:
        cargs.append("Qz")
    if delaunay_visible is not None:
        cargs.extend([
            "QGn",
            delaunay_visible
        ])
    if delaunay_regions is not None:
        cargs.extend([
            "QVn",
            delaunay_regions
        ])
    if trace_level is not None:
        cargs.extend([
            "T4",
            str(trace_level)
        ])
    if check:
        cargs.append("Tc")
    if statistics_:
        cargs.append("Ts")
    if verify:
        cargs.append("Tv")
    if output_stdout:
        cargs.append("Tz")
    if facets_summary is not None:
        cargs.extend([
            "TFn",
            str(facets_summary)
        ])
    if input_file_option is not None:
        cargs.extend([
            "TI",
            execution.input_file(input_file_option)
        ])
    if output_file_option is not None:
        cargs.extend([
            "TO",
            execution.input_file(output_file_option)
        ])
    if trace_point is not None:
        cargs.extend([
            "TPn",
            str(trace_point)
        ])
    if trace_merge is not None:
        cargs.extend([
            "TMn",
            str(trace_merge)
        ])
    if trace_merge_width is not None:
        cargs.extend([
            "TWn",
            str(trace_merge_width)
        ])
    if stop_point is not None:
        cargs.extend([
            "TVn",
            str(stop_point)
        ])
    if stop_cone_point is not None:
        cargs.extend([
            "TCn",
            str(stop_cone_point)
        ])
    if centrum_radius is not None:
        cargs.extend([
            "Cn",
            str(centrum_radius)
        ])
    if max_angle_cosine is not None:
        cargs.extend([
            "An",
            str(max_angle_cosine)
        ])
    if perturb_factor is not None:
        cargs.extend([
            "Rn",
            str(perturb_factor)
        ])
    if min_facet_width is not None:
        cargs.extend([
            "Wn",
            str(min_facet_width)
        ])
    if facet_dump:
        cargs.append("f")
    if geomview:
        cargs.append("G")
    if vertices_incident:
        cargs.append("i")
    if mathematica:
        cargs.append("m")
    if off_format:
        cargs.append("o")
    if point_coordinates:
        cargs.append("p")
    if summary:
        cargs.append("s")
    ret = QdelaunayOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "QDELAUNAY_METADATA",
    "QdelaunayOutputs",
    "qdelaunay",
]
