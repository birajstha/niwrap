# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

IMAGE_MATH_METADATA = Metadata(
    id="052c1ac1153dd70acc4761019f14bff073172224.boutiques",
    name="ImageMath",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


class ImageMathOutputs(typing.NamedTuple):
    """
    Output object returned when calling `image_math(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image: OutputPathType
    """The resulting image after processing."""


def image_math(
    image_dimension: typing.Literal[2, 3, 4],
    output_image: InputPathType,
    image1: InputPathType,
    image2: InputPathType | None = None,
    runner: Runner | None = None,
) -> ImageMathOutputs:
    """
    A versatile tool for performing various mathematical and manipulation operations
    on images.
    
    Author: ANTs developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        image_dimension: The dimensionality of the image. Use 2 or 3 for\
            spatial images, and 4 for 4D images like time-series data.
        output_image: The output image file resulting from the operations.
        image1: The first input image for the operation.
        image2: The second input image for the operation, if required.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ImageMathOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IMAGE_MATH_METADATA)
    cargs = []
    cargs.append("ImageMath")
    cargs.append(str(image_dimension))
    cargs.append(execution.input_file(output_image))
    cargs.append("[operations")
    cargs.append("and")
    cargs.append("inputs]")
    cargs.append(execution.input_file(image1))
    if image2 is not None:
        cargs.append(execution.input_file(image2))
    ret = ImageMathOutputs(
        root=execution.output_file("."),
        output_image=execution.output_file(pathlib.Path(output_image).name),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "IMAGE_MATH_METADATA",
    "ImageMathOutputs",
    "image_math",
]