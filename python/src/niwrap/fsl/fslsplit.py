# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FSLSPLIT_METADATA = Metadata(
    id="6b510a54f0a3945dad20c810310f5fdfe65d9847",
    name="fslsplit",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class FslsplitOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslsplit(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfiles: OutputPathType | None
    """Output volumes/slices"""


def fslsplit(
    infile: InputPathType,
    output_basename: str | None = "vol",
    separation_time: bool = False,
    separation_x: bool = False,
    separation_y: bool = False,
    separation_z: bool = False,
    runner: Runner = None,
) -> FslsplitOutputs:
    """
    fslsplit by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    Split a 4D image into separate volumes or a 3D image into separate slices.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Fslutils
    
    Args:
        infile: Input image (e.g. img.nii.gz).
        output_basename: Output basename (default: vol).
        separation_time: Separate images in time (default behaviour).
        separation_x: Separate images in the x direction.
        separation_y: Separate images in the y direction.
        separation_z: Separate images in the z direction.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslsplitOutputs`).
    """
    runner = runner or get_global_runner()
    if (
        separation_time +
        separation_x +
        separation_y +
        separation_z
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "separation_time,\n"
            "separation_x,\n"
            "separation_y,\n"
            "separation_z"
        )
    execution = runner.start_execution(FSLSPLIT_METADATA)
    cargs = []
    cargs.append("fslsplit")
    cargs.append(execution.input_file(infile))
    if output_basename is not None:
        cargs.append(output_basename)
    if separation_z:
        cargs.append("-z")
    ret = FslsplitOutputs(
        root=execution.output_file("."),
        outfiles=execution.output_file(f"{output_basename}????.nii.gz") if output_basename is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLSPLIT_METADATA",
    "FslsplitOutputs",
    "fslsplit",
]
