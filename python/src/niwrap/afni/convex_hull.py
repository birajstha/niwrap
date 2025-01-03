# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CONVEX_HULL_METADATA = Metadata(
    id="945c8df244e1356a8e523e12b46e0aa912eddb4c.boutiques",
    name="ConvexHull",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class ConvexHullOutputs(typing.NamedTuple):
    """
    Output object returned when calling `convex_hull(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_surf: OutputPathType | None
    """Output surface file"""


def convex_hull(
    vol: InputPathType | None = None,
    isoval: float | None = None,
    isorange: list[float] | None = None,
    isocmask: str | None = None,
    xform: str | None = None,
    surface_input: InputPathType | None = None,
    surf_vol: InputPathType | None = None,
    input_1d: InputPathType | None = None,
    q_opt: str | None = None,
    proj_xy: bool = False,
    orig_coord: bool = False,
    these_coords: InputPathType | None = None,
    output_prefix: str | None = None,
    debug: str | None = None,
    novolreg: bool = False,
    setenv: str | None = None,
    runner: Runner | None = None,
) -> ConvexHullOutputs:
    """
    A program to find the convex hull, or perform a Delaunay triangulation of a set
    of points.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        vol: Input AFNI (or AFNI readable) volume.
        isoval: Create isosurface where volume = V.
        isorange: Create isosurface where V0 <= volume < V1.
        isocmask: Create isosurface where MASK_COM != 0. Example: -isocmask '-a\
            VOL+orig -expr (1-bool(a-V))' is equivalent to using -isoval V. NOTE:\
            Allowed only with -xform mask.
        xform: Transform to apply to volume values before searching for sign\
            change boundary. Options: mask, shift, none.
        surface_input: Input surface type.
        surf_vol: Specify a surface volume which contains a transform to apply\
            to the surface node coordinates.
        input_1d: Construct the triangulation of the points contained in 1D\
            file XYZ. Use AFNI's [] selectors to specify the XYZ columns.
        q_opt: Meshing option OPT. Options: convex_hull, triangulate_xy.
        proj_xy: Project points onto plane whose normal is the third principal\
            component. Then rotate projection so that plane is parallel to Z =\
            constant.
        orig_coord: Use original coordinates when writing surface, not\
            transformed ones.
        these_coords: Use coordinates in COORDS.1D when writing surface.
        output_prefix: Prefix of output surface. Specifies the format and\
            prefix of the surface.
        debug: Debugging level.
        novolreg: Ignore any Rotate, Volreg, Tagalign, or WarpDrive\
            transformations present in the Surface Volume.
        setenv: Set environment variable ENVname to be ENVvalue.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ConvexHullOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONVEX_HULL_METADATA)
    cargs = []
    cargs.append("ConvexHull")
    if vol is not None:
        cargs.extend([
            "-input",
            execution.input_file(vol)
        ])
    if isoval is not None:
        cargs.extend([
            "-isoval",
            str(isoval)
        ])
    if isorange is not None:
        cargs.extend([
            "-isorange",
            *map(str, isorange)
        ])
    if isocmask is not None:
        cargs.extend([
            "-isocmask",
            isocmask
        ])
    if xform is not None:
        cargs.extend([
            "-xform",
            xform
        ])
    if surface_input is not None:
        cargs.extend([
            "-i_TYPE",
            execution.input_file(surface_input)
        ])
    if surf_vol is not None:
        cargs.extend([
            "-sv",
            execution.input_file(surf_vol)
        ])
    if input_1d is not None:
        cargs.extend([
            "-input_1D",
            execution.input_file(input_1d)
        ])
    if q_opt is not None:
        cargs.extend([
            "-q_opt",
            q_opt
        ])
    if proj_xy:
        cargs.append("-proj_xy")
    if orig_coord:
        cargs.append("-orig_coord")
    if these_coords is not None:
        cargs.extend([
            "-these_coords",
            execution.input_file(these_coords)
        ])
    if output_prefix is not None:
        cargs.extend([
            "-o_TYPE",
            output_prefix
        ])
    if debug is not None:
        cargs.extend([
            "-debug",
            debug
        ])
    if novolreg:
        cargs.append("-novolreg")
    if setenv is not None:
        cargs.extend([
            "-setenv",
            setenv
        ])
    ret = ConvexHullOutputs(
        root=execution.output_file("."),
        out_surf=execution.output_file(output_prefix) if (output_prefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CONVEX_HULL_METADATA",
    "ConvexHullOutputs",
    "convex_hull",
]
