# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FLIRT_AVERAGE_METADATA = Metadata(
    id="a4ca5908b5b6fca536c19df2fa885d897d7e6c95",
    name="flirt_average",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class FlirtAverageOutputs(typing.NamedTuple):
    """
    Output object returned when calling `flirt_average(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Averaged output image"""


def flirt_average(
    ninputs: int,
    input1: InputPathType,
    input2: InputPathType,
    output_file: str,
    input3: InputPathType | None = None,
    reference_image: InputPathType | None = None,
    flirt_options: str | None = None,
    runner: Runner = None,
) -> FlirtAverageOutputs:
    """
    flirt_average by FMRIB Analysis Group, Oxford Centre for Functional MRI of the
    Brain.
    
    Averages multiple input images after linear registration (FLIRT).
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FLIRT
    
    Args:
        ninputs: Number of input images.
        input1: First input image (e.g. rawT1_1.nii.gz).
        input2: Second input image (e.g. rawT1_2.nii.gz).
        output_file: Output image (e.g. averageT1.nii.gz).
        input3: Third input image (e.g. rawT1_3.nii.gz).
        reference_image: Reference image to use instead of first input.
        flirt_options: Options to be passed to FLIRT.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FlirtAverageOutputs`).
    """
    runner = runner or get_global_runner()
    if not (2 <= ninputs): 
        raise ValueError(f"'ninputs' must be greater than 2 <= x but was {ninputs}")
    execution = runner.start_execution(FLIRT_AVERAGE_METADATA)
    cargs = []
    cargs.append("flirt_average")
    cargs.append(str(ninputs))
    cargs.append(execution.input_file(input1))
    cargs.append(execution.input_file(input2))
    cargs.append("...")
    cargs.append(output_file)
    if reference_image is not None:
        cargs.extend(["-FAref", execution.input_file(reference_image)])
    if flirt_options is not None:
        cargs.append(flirt_options)
    ret = FlirtAverageOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(f"{output_file}.nii.gz", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FLIRT_AVERAGE_METADATA",
    "FlirtAverageOutputs",
    "flirt_average",
]
