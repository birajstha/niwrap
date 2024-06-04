# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FSLROI_METADATA = Metadata(
    id="0c3f4e8996b417d8b36c2d1d89abe5a943373a69",
    name="fslroi",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class FslroiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslroi(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Output file containing the extracted ROI"""


def fslroi(
    infile: InputPathType,
    outfile: str,
    xmin: float | int | None = None,
    xsize: float | int | None = None,
    ymin: float | int | None = None,
    ysize: float | int | None = None,
    zmin: float | int | None = None,
    zsize: float | int | None = None,
    tmin: float | int | None = None,
    tsize: float | int | None = None,
    runner: Runner = None,
) -> FslroiOutputs:
    """
    fslroi by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    Extracts a region of interest (ROI) from an image.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Fslutils
    
    Args:
        infile: Input image file
        outfile: Output image file
        xmin: Minimum X coordinate for ROI (indexing starts at 0)
        xsize: Size of the ROI in X direction
        ymin: Minimum Y coordinate for ROI (indexing starts at 0)
        ysize: Size of the ROI in Y direction
        zmin: Minimum Z coordinate for ROI (indexing starts at 0)
        zsize: Size of the ROI in Z direction
        tmin: Minimum T coordinate for ROI (indexing starts at 0)
        tsize: Size of the ROI in T direction
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `FslroiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLROI_METADATA)
    cargs = []
    cargs.append("fslroi")
    cargs.append(execution.input_file(infile))
    cargs.append(outfile)
    if xmin is not None:
        cargs.append(str(xmin))
    if xsize is not None:
        cargs.append(str(xsize))
    if ymin is not None:
        cargs.append(str(ymin))
    if ysize is not None:
        cargs.append(str(ysize))
    if zmin is not None:
        cargs.append(str(zmin))
    if zsize is not None:
        cargs.append(str(zsize))
    if tmin is not None:
        cargs.append(str(tmin))
    if tsize is not None:
        cargs.append(str(tsize))
    ret = FslroiOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(f"{outfile}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLROI_METADATA",
    "FslroiOutputs",
    "fslroi",
]
