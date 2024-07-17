# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

ROIGROW_METADATA = Metadata(
    id="4bdd538e5abcecd43fd21c32330e81a8e1ad71b1",
    name="ROIgrow",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class RoigrowOutputs(typing.NamedTuple):
    """
    Output object returned when calling `roigrow(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType | None
    """1D output dataset."""


def roigrow(
    input_surface: str,
    roi_labels: str,
    lim_distance: float | int,
    output_prefix: str | None = None,
    full_list: bool = False,
    grow_from_edge: bool = False,
    insphere_diameter: float | int | None = None,
    inbox_edges: list[float | int] | None = None,
    runner: Runner | None = None,
) -> RoigrowOutputs:
    """
    ROIgrow by AFNI Team.
    
    A program to expand an ROI on the surface.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/ROIgrow.html
    
    Args:
        input_surface: Specify input surface. You can also use -t* and -spec\
            and -surf methods to input surfaces.
        roi_labels: Data column containing integer labels of ROIs. Each integer\
            label gets grown separately.
        lim_distance: Distance to cover from each node. The units of LIM are\
            those of the surface's node coordinates. Distances are calculated along\
            the surface's mesh.
        output_prefix: Prefix of 1D output dataset. Default is ROIgrow.
        full_list: Output a row for each node on the surface. Nodes not in the\
            grown ROI, receive a 0 for a label. This option is ONLY for use with\
            -roi_labels.
        grow_from_edge: Grow ROIs from their edges rather than the brute force\
            default. This might make the program faster on large ROIs and large\
            surfaces.
        insphere_diameter: Diameter of the sphere inside which nodes are added\
            instead of growing along the surface.
        inbox_edges: Use a box of edge widths E1, E2, E3 instead of DIA.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RoigrowOutputs`).
    """
    runner = runner or get_global_runner()
    if inbox_edges is not None and (len(inbox_edges) != 3): 
        raise ValueError(f"Length of 'inbox_edges' must be 3 but was {len(inbox_edges)}")
    execution = runner.start_execution(ROIGROW_METADATA)
    cargs = []
    cargs.append("ROIgrow")
    cargs.append("<-i_TYPE")
    cargs.append("SURF>")
    cargs.append("<-roi_labels")
    cargs.append("ROI_LABELS>")
    cargs.append("<-lim")
    cargs.append("LIM>")
    cargs.append("[-prefix")
    cargs.append("PREFIX]")
    if full_list:
        cargs.append("-full_list")
    if grow_from_edge:
        cargs.append("-grow_from_edge")
    if insphere_diameter is not None:
        cargs.extend(["-insphere", str(insphere_diameter)])
    if inbox_edges is not None:
        cargs.extend(["-inbox", *map(str, inbox_edges)])
    ret = RoigrowOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(f"{output_prefix}.1D", optional=True) if output_prefix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ROIGROW_METADATA",
    "RoigrowOutputs",
    "roigrow",
]
