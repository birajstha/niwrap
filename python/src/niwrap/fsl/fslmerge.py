# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FSLMERGE_METADATA = Metadata(
    id="b8617d0d3b90cca3d6ad99d8535a2ae1e85525b5",
    name="fslmerge",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class FslmergeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslmerge(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Output concatenated image file"""


def fslmerge(
    output_file: str,
    input_files: list[InputPathType],
    merge_time: bool = False,
    merge_x: bool = False,
    merge_y: bool = False,
    merge_z: bool = False,
    auto_choose: bool = False,
    merge_set_tr: bool = False,
    volume_number: float | int | None = None,
    tr_value: float | int | None = None,
    runner: Runner = None,
) -> FslmergeOutputs:
    """
    fslmerge by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    FSL tool to concatenate images in various dimensions.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Fslutils
    
    Args:
        output_file: Output concatenated image file.
        input_files: Input image files to concatenate.
        merge_time: Concatenate images in time (4th dimension).
        merge_x: Concatenate images in the x direction.
        merge_y: Concatenate images in the y direction.
        merge_z: Concatenate images in the z direction.
        auto_choose: Auto-choose: single slices -> volume, volumes -> 4D (time\
            series).
        merge_set_tr: Concatenate images in time and set the output image tr to\
            the provided value.
        volume_number: Only use volume <N> from each input file (first volume\
            is 0 not 1).
        tr_value: TR value in seconds, used with the -tr flag.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslmergeOutputs`).
    """
    runner = runner or get_global_runner()
    if (
        merge_time +
        merge_x +
        merge_y +
        merge_z +
        auto_choose +
        merge_set_tr
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "merge_time,\n"
            "merge_x,\n"
            "merge_y,\n"
            "merge_z,\n"
            "auto_choose,\n"
            "merge_set_tr"
        )
    execution = runner.start_execution(FSLMERGE_METADATA)
    cargs = []
    cargs.append("fslmerge")
    if merge_set_tr:
        cargs.append("-tr")
    cargs.append(output_file)
    cargs.extend([execution.input_file(f) for f in input_files])
    if tr_value is not None:
        cargs.append(str(tr_value))
    ret = FslmergeOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(f"{output_file}.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLMERGE_METADATA",
    "FslmergeOutputs",
    "fslmerge",
]
