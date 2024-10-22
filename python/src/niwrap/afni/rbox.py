# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

RBOX_METADATA = Metadata(
    id="80319d4648d635c07c7e3bce7e954e3b8fe64128.boutiques",
    name="rbox",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class RboxOutputs(typing.NamedTuple):
    """
    Output object returned when calling `rbox(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def rbox(
    number_points: str,
    dimension: str | None = None,
    integer_coordinates: bool = False,
    bounding_box: float | None = None,
    offset: float | None = None,
    user_seed: float | None = None,
    mesh_lattice: list[str] | None = None,
    runner: Runner | None = None,
) -> RboxOutputs:
    """
    Generate various point distributions. Default is random in cube.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        number_points: Number of random points in cube, lens, spiral, sphere or\
            grid.
        dimension: Dimension (e.g., D3 for 3-d).
        integer_coordinates: Print integer coordinates, default 'Bn' is 1e+06.
        bounding_box: Bounding box coordinates, default 0.5.
        offset: Offset coordinates by n.
        user_seed: Use n as the random number seed.
        mesh_lattice: Lattice (Mesh) rotated by [n,-m,0], [m,n,0], [0,0,r], ...
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RboxOutputs`).
    """
    if mesh_lattice is not None and not (3 <= len(mesh_lattice)): 
        raise ValueError(f"Length of 'mesh_lattice' must be greater than 3 but was {len(mesh_lattice)}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(RBOX_METADATA)
    cargs = []
    cargs.append("rbox")
    cargs.append(number_points)
    if dimension is not None:
        cargs.append(dimension)
    if integer_coordinates:
        cargs.append("z")
    if bounding_box is not None:
        cargs.extend([
            "B",
            str(bounding_box)
        ])
    if offset is not None:
        cargs.extend([
            "O",
            str(offset)
        ])
    if user_seed is not None:
        cargs.extend([
            "t",
            str(user_seed)
        ])
    if mesh_lattice is not None:
        cargs.extend([
            "M",
            *mesh_lattice
        ])
    ret = RboxOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "RBOX_METADATA",
    "RboxOutputs",
    "rbox",
]
