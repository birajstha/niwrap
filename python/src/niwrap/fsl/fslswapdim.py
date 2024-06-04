# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FSLSWAPDIM_METADATA = Metadata(
    id="2073e53151fd9f2ea94a307a6ce4171d47e2fb20",
    name="fslswapdim",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class FslswapdimOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslswapdim(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image: OutputPathType | None
    """Output image with swapped dimensions"""


def fslswapdim(
    input_file: InputPathType,
    axis_a: str,
    axis_b: str,
    axis_c: str,
    output_file: str | None = None,
    runner: Runner = None,
) -> FslswapdimOutputs:
    """
    fslswapdim by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    Swap dimensions of an image volume.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Fslutils
    
    Args:
        input_file: Input image (e.g. img.nii.gz)
        axis_a: New x-axis dimension (e.g., -x, x, RL, etc.)
        axis_b: New y-axis dimension (e.g., -y, y, PA, etc.)
        axis_c: New z-axis dimension (e.g., -z, z, IS, etc.)
        output_file: Output image (e.g., output.nii.gz). If not specified, the
            equivalent transformation matrix is written to the standard output.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `FslswapdimOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLSWAPDIM_METADATA)
    cargs = []
    cargs.append("fslswapdim")
    cargs.append(execution.input_file(input_file))
    cargs.append(axis_a)
    cargs.append(axis_b)
    cargs.append(axis_c)
    if output_file is not None:
        cargs.append(output_file)
    ret = FslswapdimOutputs(
        root=execution.output_file("."),
        output_image=execution.output_file(f"{output_file}", optional=True) if output_file is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLSWAPDIM_METADATA",
    "FslswapdimOutputs",
    "fslswapdim",
]
