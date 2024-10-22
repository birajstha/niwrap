# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CREATE_DISPLACEMENT_FIELD_METADATA = Metadata(
    id="f31aab764e07d12987a50a4b593617b99c684fb3.boutiques",
    name="CreateDisplacementField",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


class CreateDisplacementFieldOutputs(typing.NamedTuple):
    """
    Output object returned when calling `create_displacement_field(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_displacement_field: OutputPathType
    """The generated itkImage of itkVector pixels representing the displacement
    field."""


def create_displacement_field(
    image_dimension: int,
    enforce_zero_boundary_flag: typing.Literal[0, 1],
    component_images: list[InputPathType],
    output_image: InputPathType,
    runner: Runner | None = None,
) -> CreateDisplacementFieldOutputs:
    """
    Create an itkImage of itkVector pixels (NOT an itkVectorImage), using each
    scalar input component image for each vector component. An itkImage of
    itkVectors is the standard type for displacement fields in ITK. All component
    images (up to 8) are assumed to have the same size, offset, origin, and spacing.
    The 'EnforceZeroBoundaryFlag' option will create zero-valued vectors along the
    borders when enabled (pass 1), and is recommended for better displacement field
    behavior.
    
    Author: ANTs developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        image_dimension: The dimension of the image, typically 2 or 3.
        enforce_zero_boundary_flag: Create zero-valued vectors along the\
            borders when enabled (pass 1), recommended for better displacement\
            field behavior.
        component_images: Input component images, each used for a vector\
            component. All component images must have the same size, offset,\
            origin, and spacing.
        output_image: The output displacement field image with itkVector\
            pixels.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CreateDisplacementFieldOutputs`).
    """
    if not (1 <= len(component_images) <= 8): 
        raise ValueError(f"Length of 'component_images' must be between 1 and 8 but was {len(component_images)}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(CREATE_DISPLACEMENT_FIELD_METADATA)
    cargs = []
    cargs.append("CreateDisplacementField")
    cargs.append(str(image_dimension))
    cargs.append(str(enforce_zero_boundary_flag))
    cargs.extend([execution.input_file(f) for f in component_images])
    cargs.append(execution.input_file(output_image))
    ret = CreateDisplacementFieldOutputs(
        root=execution.output_file("."),
        output_displacement_field=execution.output_file(pathlib.Path(output_image).name),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CREATE_DISPLACEMENT_FIELD_METADATA",
    "CreateDisplacementFieldOutputs",
    "create_displacement_field",
]
