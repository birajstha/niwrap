# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

I_MATH_METADATA = Metadata(
    id="fe31e452a5266b32b2e5e22ffbb63f2ff9cf99e1.boutiques",
    name="iMath",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


class IMathOutputs(typing.NamedTuple):
    """
    Output object returned when calling `i_math(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    resulting_image: OutputPathType
    """The output image resulting from the operation."""


def i_math(
    image_dimension: typing.Literal[2, 3, 4],
    output_image: str,
    operations: str,
    image1: InputPathType,
    image2: InputPathType | None = None,
    runner: Runner | None = None,
) -> IMathOutputs:
    """
    iMath is a tool for performing various image mathematical operations on medical
    images, specifically supporting operations on 2D, 3D, and 4D data.
    
    Author: ANTs developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        image_dimension: Dimensionality of the image, either 2, 3, or 4.
        output_image: Path for the output image file.
        operations: Operations to be performed along with parameters, e.g.,\
            GetLargestComponent, MC for Closing, etc.
        image1: First input image file.
        image2: Second input image file, if required by operation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `IMathOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(I_MATH_METADATA)
    cargs = []
    cargs.append("iMath")
    cargs.append(str(image_dimension))
    cargs.append(output_image)
    cargs.append(operations)
    cargs.append(execution.input_file(image1))
    if image2 is not None:
        cargs.append(execution.input_file(image2))
    ret = IMathOutputs(
        root=execution.output_file("."),
        resulting_image=execution.output_file(output_image),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "IMathOutputs",
    "I_MATH_METADATA",
    "i_math",
]
