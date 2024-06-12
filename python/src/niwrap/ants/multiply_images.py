# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

MULTIPLY_IMAGES_METADATA = Metadata(
    id="caea37918e8cd3ce060ab9e00b19c02e344bf21e",
    name="MultiplyImages",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class MultiplyImagesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `multiply_images(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_product_image_outfile: OutputPathType
    """Average image file."""


def multiply_images(
    dimension: typing.Literal[3, 2],
    first_input: InputPathType,
    output_product_image: InputPathType,
    num_threads: int | None = 1,
    second_input: InputPathType | None = None,
    second_input_2: float | int | None = None,
    runner: Runner = None,
) -> MultiplyImagesOutputs:
    """
    MultiplyImages by Nipype (interface).
    
    No description provided.
    
    Args:
        dimension: 3 or 2. Image dimension (2 or 3).
        first_input: Image 1.
        output_product_image: Outputfname.nii.gz: the name of the resulting\
            image.
        num_threads: Number of itk threads to use.
        second_input: file or string or a float. Image 2 or multiplication\
            weight.
        second_input_2: file or string or a float. Image 2 or multiplication\
            weight.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MultiplyImagesOutputs`).
    """
    runner = runner or get_global_runner()
    if (
        (second_input is not None) +
        (second_input_2 is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "second_input,\n"
            "second_input_2"
        )
    execution = runner.start_execution(MULTIPLY_IMAGES_METADATA)
    cargs = []
    cargs.append("MultiplyImages")
    cargs.append(str(dimension))
    cargs.append(execution.input_file(first_input))
    if second_input_2 is not None:
        cargs.append(str(second_input_2))
    cargs.append(execution.input_file(output_product_image))
    if num_threads is not None:
        cargs.append(str(num_threads))
    ret = MultiplyImagesOutputs(
        root=execution.output_file("."),
        output_product_image_outfile=execution.output_file(f"{pathlib.Path(output_product_image).name}", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MULTIPLY_IMAGES_METADATA",
    "MultiplyImagesOutputs",
    "multiply_images",
]
